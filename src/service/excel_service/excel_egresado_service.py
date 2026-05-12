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
            df = pd.read_excel(io.BytesIO(contenido))
            df.columns = df.columns.str.strip()

            exitosos = []
            fallidos  = []

            for indice, fila in df.iterrows():
                numero_fila = indice + 2
                try:
                    datos = {
                        k: (None if pd.isna(v) else v)
                        for k, v in fila.to_dict().items()
                    }

                    for campo_bool in ("discapacidad", "carnet", "dominioSegundaLengua", "produccionIntelectual"):
                        if datos.get(campo_bool) is not None:
                            datos[campo_bool] = str(datos[campo_bool]).strip().lower() in ("true", "1", "sí", "si", "verdadero")

                    for campo_int in ("estratoSocioeconomico", "experiencia", "idPrograma"):
                        if datos.get(campo_int) is not None:
                            datos[campo_int] = int(float(datos[campo_int]))
                            
                    for campo_str in ("numeroDocumento", "telefono"):
                        if datos.get(campo_str) is not None:
                            datos[campo_str] = str(int(float(datos[campo_str])))

                    if datos.get("fechaNacimiento") is not None:
                        datos["fechaNacimiento"] = str(datos["fechaNacimiento"]).strip()[:10]
                        
                    if datos.get("nombrePrograma") is not None:
                        programa = supabase.table("Programas") \
                            .select("idPrograma") \
                            .eq("nombrePrograma", datos.pop("nombrePrograma")) \
                            .single() \
                            .execute()
                        
                        if not programa.data:
                            raise ValueError(f"No existe un programa con el nombre '{datos.get('nombrePrograma')}'")
                        
                        datos["idPrograma"] = programa.data["idPrograma"]

                    egresado_dto = EgresadoDto(**datos)
                    resultado = await EgresadoService.crear_egresado(egresado_dto)

                    if "error" in resultado:
                        fallidos.append({"fila": numero_fila, "motivo": resultado["error"]})
                    else:
                        exitosos.append(numero_fila)

                except Exception as e:
                    fallidos.append({"fila": numero_fila, "motivo": str(e)})

            return {
                "total_procesadas": len(exitosos) + len(fallidos),
                "exitosos": len(exitosos),
                "fallidos": len(fallidos),
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