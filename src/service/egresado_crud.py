from fastapi import HTTPException

from src.modelDto.egresado_dto import EgresadoDto
from src.config.supabase_client import supabase

class EgresadoService:


    async def crear_egresado(egresado: EgresadoDto):
        try:
            existeEgresado = supabase.table("Egresados")\
                .select("idEgresado")\
                .eq("numeroDocumento", egresado.numeroDocumento).execute()
            
            if existeEgresado.data:
                raise HTTPException(status_code=404, detail="El egresado ya existe")

            response = supabase.table('Egresados').insert(egresado.model_dump(mode='json')).execute()
            return {"message": "Egresado creado exitosamente", "data": response.data}
        
        except Exception as e:
            return {"message": "Error al crear el egresado", "error": str(e)}
            

    async def get_egresados():
        try:
            response = supabase.table('egresados').select('*').execute()
            return response.data
        except Exception as e:
            return {"message": "Error al obtener los egresados", "error": str(e)}
    
    async def get_egresado_by_id(idEgresado: int):
        try:
            response = supabase.table('egresados').select('*').eq('idEgresado', idEgresado).execute()
            if not response.data:
                raise HTTPException(status_code=404, detail="Egresado no encontrado")
            return response.data[0]
        except Exception as e:
            return {"message": "Error al obtener el egresado", "error": str(e)}


    async def eliminar_egresado(idEgresado: int):
        try:
            response = supabase.table('egresados').delete().eq('idEgresado', idEgresado).execute()
            if response.count == 0:
                raise HTTPException(status_code=404, detail="Egresado no encontrado")
        except Exception as e:
            return {"message": "Error al eliminar el egresado", "error": str(e)}

    