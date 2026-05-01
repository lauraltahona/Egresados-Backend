from fastapi import HTTPException

from src.modelDto.egresado_dto import EgresadoDto
from src.config.supabase_client import supabase

class EgresadoService:

    @staticmethod
    def crear_egresado(egresado: EgresadoDto):
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
            

    @staticmethod
    def get_egresados():
        response = supabase.table('egresados').select('*').execute()
        return response.data