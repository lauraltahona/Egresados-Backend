from fastapi import HTTPException

from src.modelDto.situacionLaboral_dto import SituacionLaboralDto
from src.repository.reporte_repository import limpiar_cache

from src.config.supabase_client import supabase

class SituacionLaboralService:

    async def crear_situacion_laboral(situacion: SituacionLaboralDto):
        try:
            print(situacion)
            print(supabase)
            existeEgresado = supabase.table("Egresados")\
                .select("idEgresado, nombreEgresado, apellidosEgresado")\
                .eq("idEgresado", situacion.idEgresado).execute()
            
            if not existeEgresado.data: raise HTTPException(status_code=404, detail="El egresado no existe")

            response = supabase.table("situacionLaboral")\
                .insert(situacion.model_dump(mode='json')).execute()
            
            limpiar_cache()
            
            return {"message": "Situación laboral creada exitosamente"}
        
        except HTTPException as e:
            raise e
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al crear la situacion laboral:{str(e)}")
        

    async def obtener_situacion_laboral_por_egresado(idEgresado: int):
        try:
            response = (
                supabase.table("situacionLaboral")
                .select("""
                    *,
                    Egresados(
                        nombreEgresado,
                        apellidosEgresado
                    )
                """)
                .eq("idEgresado", idEgresado)
                .execute()
            )

            if not response.data:
                return {"error": "No se encontró la situación laboral para el egresado especificado"}

            return {"data": response.data[0]}

        except HTTPException as e:
            raise e
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al obtener la situacion laboral:{str(e)}")
        

    async def get_situacion_laboral():
        try:
            response = (
                supabase.table("situacionLaboral")
                .select("""
                    *,
                    Egresados(
                        nombreEgresado,
                        apellidosEgresado
                    )
                """)
                .execute()
           )

            return {"data": response.data}

        except HTTPException as e:
            raise e
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al obtener las situaciones laborales: {str(e)}")




    async def actualizar_situacion_laboral(idSituacion: int, situacion: dict):
        try:
            response = supabase.table("situacionLaboral")\
                .update(situacion.dict())\
                .eq("idSituacion", idSituacion).execute()
            
            if response.status_code != 200:
                return {"error": "No se pudo actualizar la situación laboral"}
            
            limpiar_cache()
            
            return {"message": "Situación laboral actualizada exitosamente", "data": response.data}
        
        except Exception as e:
            return {"error": str(e)}

