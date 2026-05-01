from fastapi import HTTPException

from src.modelDto.situacionLaboral_dto import SituacionLaboralDto
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
            
            return {"message": "Situación laboral creada exitosamente"}
            
        except Exception as e:
            return {"error": str(e)}
        

    async def obtener_situacion_laboral_por_egresado(idEgresado: int):
        try:
            response = supabase.table("SituacionesLaborales")\
                .select("*")\
                .eq("idEgresado", idEgresado).execute()
            if not response.data:
                return {"error": "No se encontró la situación laboral para el egresado especificado"}
            return {"data": response.data[0]}
        
        except Exception as e:
            return {"error": str(e)}

    async def actualizar_situacion_laboral(idSituacion: int, situacion: dict):
        try:
            response = supabase.table("SituacionesLaborales")\
                .update(situacion.dict())\
                .eq("idSituacion", idSituacion).execute()
            
            if response.status_code != 200:
                return {"error": "No se pudo actualizar la situación laboral"}
            
            return {"message": "Situación laboral actualizada exitosamente", "data": response.data}
        
        except Exception as e:
            return {"error": str(e)}

