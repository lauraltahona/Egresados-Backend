from src.modelDto.publicacionComunidad_dto import PublicacionComunidadDto
from src.config.supabase_client import supabase
from fastapi import HTTPException

class PublicacionComunidadService:

    async def crear_publicacion_comunidad(publicacion_dto: PublicacionComunidadDto):
        try:
            validarMiembro = supabase.table("MiembrosComunidades")\
                .select("idMiembro")\
                .eq("idEgresado", publicacion_dto.idEgresado).eq("idComunidad", publicacion_dto.idComunidad)\
                .execute()
            
            if not validarMiembro.data:
                raise HTTPException(status_code=404, detail="El egresado no es miembro de la comunidad")
            
            response = supabase.table("PublicacionesComunidades")\
                .insert(publicacion_dto.model_dump(mode="json")).execute()
            
            return {"message": "Publicación creada exitosamente", "data": response.data}
        
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al crear la publicación: {str(e)}")
        

