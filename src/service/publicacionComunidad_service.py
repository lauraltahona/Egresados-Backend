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
        
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al crear la publicación: {str(e)}")
        

    async def get_publicaciones_comunidad(idComunidad: int):
        try:
            response = supabase.table("PublicacionesComunidades")\
                .select("*")\
                .eq("idComunidad", idComunidad)\
                .execute()
            
            if not response.data:
                raise HTTPException(status_code=404, detail="No se encontraron publicaciones para esta comunidad")
            
            return {"data": response.data}
        
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al obtener las publicaciones: {str(e)}")
        
    async def eliminar_publicacion_comunidad(idPublicacion: int, idEgresado: int):
        try:
            validarPublicacion = supabase.table("PublicacionesComunidades")\
                .select("idPublicacion")\
                .eq("idPublicacion", idPublicacion)\
                .eq("idEgresado", idEgresado)\
                .execute()

            if not validarPublicacion.data:
                raise HTTPException(status_code=404, detail="La publicación no existe o no pertenece al egresado")

            response = supabase.table("PublicacionesComunidades")\
                .delete()\
                .eq("idPublicacion", idPublicacion)\
                .execute()

            return {"message": "Publicación eliminada exitosamente"}
        
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al eliminar la publicación: {str(e)}")
        

        async def comentar_publicacion_comunidad(idPublicacion: int, idEgresado: int, comentario: str):
           pass
