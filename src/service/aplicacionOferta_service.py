from datetime import date
from fastapi import HTTPException
from src.config.supabase_client import supabase
from src.modelDto.aplicacionOferta_dto import AplicacionOfertaDto
from src.enum.aplicacionOferta_enum import EstadoAplicacion


class AplicacionOfertaService:

    async def postular_egresado(aplicacion: AplicacionOfertaDto):
        try:
            egresado = supabase.table("Egresados") \
                .select("idEgresado") \
                .eq("idEgresado", aplicacion.idEgresado) \
                .execute()

            if not egresado.data:
                raise HTTPException(status_code=404, detail="El egresado no existe")

            oferta = supabase.table("OfertasLaborales") \
                .select("idOferta") \
                .eq("idOferta", aplicacion.idOferta) \
                .execute()

            if not oferta.data:
                raise HTTPException(status_code=404, detail="La oferta laboral no existe")

            aplicacion_existente = supabase.table("AplicacionesOfertas") \
                .select("idAplicacion") \
                .eq("idEgresado", aplicacion.idEgresado) \
                .eq("idOferta", aplicacion.idOferta) \
                .execute()

            if aplicacion_existente.data:
                raise HTTPException(
                    status_code=400,
                    detail="El egresado ya se ha postulado a esta oferta"
                )

            datos = {
                "fechaAplicacion": date.today().isoformat(),
                "estadoAplicacion": EstadoAplicacion.ENVIADA,
                "idEgresado": aplicacion.idEgresado,
                "idOferta": aplicacion.idOferta,
                "cartaPresentacion": aplicacion.cartaPresentacion,
                "rutaHojaVida": aplicacion.rutaHojaVida,
            }

            response = supabase.table("AplicacionesOfertas").insert(datos).execute()

            return {"message": "Postulación realizada exitosamente", "data": response.data}

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al realizar la postulación: {str(e)}")


    async def listar_egresados_por_oferta(idOferta: int):
        try:
            # Verificar que la oferta existe
            oferta = supabase.table("OfertasLaborales") \
                .select("idOferta, tituloOferta") \
                .eq("idOferta", idOferta) \
                .execute()

            if not oferta.data:
                raise HTTPException(status_code=404, detail="La oferta laboral no existe")

            response = supabase.table("AplicacionesOfertas") \
                .select("""
                    idAplicacion,
                    fechaAplicacion,
                    estadoAplicacion,
                    cartaPresentacion,
                    rutaHojaVida,
                    fechaActualizacionEstado,
                    Egresados(
                        idEgresado,
                        nombreEgresado,
                        apellidosEgresado,
                        correoEgresado,
                        telefono
                    )
                """) \
                .eq("idOferta", idOferta) \
                .execute()

            return {
                "oferta": oferta.data[0],
                "totalPostulantes": len(response.data),
                "data": response.data
            }

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al listar los postulantes: {str(e)}")


    async def eliminar_postulacion(idAplicacion: int, idEgresado: int):
        try:
            aplicacion = supabase.table("AplicacionesOfertas") \
                .select("idAplicacion, estadoAplicacion") \
                .eq("idAplicacion", idAplicacion) \
                .eq("idEgresado", idEgresado) \
                .execute()

            if not aplicacion.data:
                raise HTTPException(
                    status_code=404,
                    detail="La postulación no existe o no pertenece al egresado"
                )

            estado = aplicacion.data[0]["estadoAplicacion"]
            if estado in (EstadoAplicacion.SELECCIONADO, EstadoAplicacion.CONTRATADO, EstadoAplicacion.EN_REVISION):
                raise HTTPException(
                    status_code=400,
                    detail=f"No se puede eliminar una postulación con estado '{estado}'"
                )

            supabase.table("AplicacionesOfertas") \
                .delete() \
                .eq("idAplicacion", idAplicacion) \
                .execute()

            return {"message": "Postulación eliminada exitosamente"}

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al eliminar la postulación: {str(e)}")


    async def actualizar_estado_aplicacion(idAplicacion: int, estado: EstadoAplicacion):
        try:
            aplicacion = supabase.table("AplicacionesOfertas") \
                .select("idAplicacion") \
                .eq("idAplicacion", idAplicacion) \
                .execute()

            if not aplicacion.data:
                raise HTTPException(status_code=404, detail="La postulación no existe")

            response = supabase.table("AplicacionesOfertas") \
                .update({
                    "estadoAplicacion": estado,
                    "fechaActualizacionEstado": date.today().isoformat()
                }) \
                .eq("idAplicacion", idAplicacion) \
                .execute()

            return {"message": f"Estado actualizado a '{estado}'", "data": response.data}

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar el estado: {str(e)}")