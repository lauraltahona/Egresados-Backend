from src.modelDto.miembroComunidad_dto import MiembroComunidadDto
from src.config.supabase_client import supabase
from fastapi import HTTPException

class MiembroComunidadService:
    
    async def crear_miembro_comunidad(miembro_comunidad_dto: MiembroComunidadDto):
        try:
            existeComunidad = supabase.table("Comunidades")\
                .select("idComunidad, nombreComunidad, descripcionComunidad")\
                .eq("idComunidad", miembro_comunidad_dto.idComunidad)\
                .execute()
            
            existeEgresado = supabase.table("Egresados")\
                .select("idEgresado, nombreEgresado")\
                .eq("idEgresado", miembro_comunidad_dto.idEgresado)\
                .execute()
            
            if not existeComunidad.data:
                raise HTTPException(status_code=404, detail="La comunidad no existe")
            
            if not existeEgresado.data:
                raise HTTPException(status_code=404, detail="El egresado no existe")
            
            response = supabase.table("MiembrosComunidades")\
                .insert(miembro_comunidad_dto.model_dump(mode='json'))\
                .execute()
            
            return {"message": "Miembro de comunidad creado exitosamente", "data": response.data}
        
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al crear el miembro de comunidad: {str(e)}")
        

    async def obtener_miembros_comunidad(idComunidad: int):
        try:
            response = supabase.table("MiembrosComunidades")\
                .select('*').eq("idComunidad", idComunidad).execute()

            return {"message": "Miembros de comunidad obtenidos exitosamente", "data": response.data}

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al obtener los miembros de comunidad: {str(e)}")

    async def eliminar_miembro_comunidad(idMiembro: int):
        try:
            response = supabase.table("MiembrosComunidades")\
                .delete().eq("idMiembro", idMiembro).execute()
            
            if response.count == 0:
                raise HTTPException(status_code=404, detail="Miembro de comunidad no encontrado")
            
            return {"message": "Miembro de comunidad eliminado exitosamente"}
        
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al eliminar el miembro de comunidad: {str(e)}")
            
