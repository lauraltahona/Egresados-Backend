import io

import pandas as pd
from fastapi import HTTPException, UploadFile
from fastapi.responses import StreamingResponse

from src.config.supabase_client import supabase
from src.modelDto.egresado_dto import EgresadoDto
from src.service.egresado_crud import EgresadoService
from src.service.excel_service.excel_service import exportar_excel

class ExcelEgresadoService:

    async def exportar_egresados() -> StreamingResponse:
        try:
            response = supabase.table("Egresados").select(
                "nombreEgresado, apellidosEgresado, tipoDocumento, numeroDocumento, "
                "fechaNacimiento, correoEgresado, telefono, sexo, grupoEtnico, "
                "discapacidad, carnet, dominioSegundaLengua, segundaLengua, "
                "Programas(nombrePrograma), paisResidencia, ciudadResidencia, departamentoResidencia, "
                "direccion, estratoSocioeconomico, nivelFormacionProfesional, "
                "produccionIntelectual, nombreProduccionIntelectual, experiencia, "
                "sexoOtro, segundaLenguaOtro"
            ).execute()

            datos = []
            for egresado in response.data:
                egresado["nombrePrograma"] = egresado.pop("Programas", {}).get("nombrePrograma")
                datos.append(egresado)

            return exportar_excel(datos, nombre_hoja="Egresados")

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al exportar egresados: {str(e)}")


    async def importar_egresados(archivo: UploadFile):
        try:
            contenido = await archivo.read()
            
            df = pd.read_excel(io.BytesIO(contenido), header=3)
            df.columns = df.columns.str.strip()
            
            campos = ["APELLIDOS Y NOMBRES", "IDENTIFICACION", "PROGRAMA", "FECHA"]
            df = df.dropna(subset=campos, how='any')
            df = df[pd.to_numeric(df["IDENTIFICACION"], errors='coerce').notna()]

            programas_response = supabase.table("Programas").select("idPrograma, nombrePrograma").execute()
            programas_map = {
                p["nombrePrograma"].strip().lower(): p["idPrograma"]
                for p in programas_response.data
            }

            exitosos = []
            fallidos = []

            for indice, fila in df.iterrows():
                numero_fila = indice + 2
                try:
                    apellidos_nombres = str(fila.get("APELLIDOS Y NOMBRES", "")).strip()
                    identificacion = str(int(float(str(fila.get("IDENTIFICACION", "")).strip())))
                    programa_nombre = str(fila.get("PROGRAMA", "")).strip()
                    fecha_grado = fila.get("FECHA")

                    if not apellidos_nombres or not identificacion or not programa_nombre or pd.isna(fecha_grado):
                        raise ValueError("Faltan datos obligatorios")

                    id_programa = programas_map.get(programa_nombre.lower())
                    if not id_programa:
                        raise ValueError(f"Programa '{programa_nombre}' no existe en la base de datos")

                    partes = apellidos_nombres.split()
                    if len(partes) < 2:
                        raise ValueError(f"Formato inválido de nombre: '{apellidos_nombres}'")

                    nombre = partes[0]
                    apellidos = " ".join(partes[1:])

                    if isinstance(fecha_grado, str):
                        fecha_grado_str = fecha_grado.strip()[:10]
                    else:
                        fecha_grado_str = pd.Timestamp(fecha_grado).strftime("%Y-%m-%d")

                    egresado_existente = supabase.table("Egresados") \
                        .select("idEgresado") \
                        .eq("numeroDocumento", identificacion) \
                        .execute()

                    if egresado_existente.data:
                        fallidos.append({
                            "fila": numero_fila,
                            "motivo": f"Egresado con identificación '{identificacion}' ya existe",
                            "tipo": "duplicado"
                        })
                        continue

                    datos_egresado = {
                        "nombreEgresado": nombre,
                        "apellidosEgresado": apellidos,
                        "numeroDocumento": identificacion,
                        "idPrograma": id_programa,
                        "fechaGrado": fecha_grado_str,
                        "esGraduado": True
                    }

                    response = supabase.table("Egresados").insert(datos_egresado).execute()
                    if response.data:
                        exitosos.append({
                            "fila": numero_fila,
                            "identificacion": identificacion,
                            "nombre": nombre,
                            "apellidos": apellidos
                        })
                    else:
                        fallidos.append({"fila": numero_fila, "motivo": "No se pudo insertar"})

                except Exception as e:
                    fallidos.append({"fila": numero_fila, "motivo": str(e)})

            return {
                "total_procesadas": len(exitosos) + len(fallidos),
                "creados": len(exitosos),
                "fallidos": len(fallidos),
                "detalle_exitosos": exitosos,
                "detalle_errores": fallidos
            }

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al procesar el archivo: {str(e)}")

    async def descargar_plantilla() -> StreamingResponse:
        columnas = [
            "nombreEgresado", "apellidosEgresado", "tipoDocumento", "numeroDocumento",
            "fechaNacimiento", "correoEgresado", "telefono", "sexo", "grupoEtnico",
            "discapacidad", "carnet", "dominioSegundaLengua", "segundaLengua",
            "nombrePrograma", "paisResidencia", "ciudadResidencia", "departamentoResidencia",
            "direccion", "estratoSocioeconomico", "nivelFormacionProfesional",
            "produccionIntelectual", "nombreProduccionIntelectual", "experiencia",
            "sexoOtro", "segundaLenguaOtro"
        ]

        buffer = io.BytesIO()
        df = pd.DataFrame(columns=columnas)

        with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="Plantilla")

            hoja = writer.sheets["Plantilla"]
            for col in hoja.columns:
                hoja.column_dimensions[col[0].column_letter].width = 25

        buffer.seek(0)

        return StreamingResponse(
            buffer,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={"Content-Disposition": "attachment; filename=plantilla_egresados.xlsx"}
        )