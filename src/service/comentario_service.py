from src.modelDto.comentario_dto import ComentarioPublicacionDto
from fastapi import HTTPException
from src.config.supabase_client import supabase

class ComentarioPublicacionService:

    async def crear_comentario(comentario: ComentarioPublicacionDto):
        try:
            existePublicacion = supabase.table("PublicacionesComunidades")\
                .select("idPublicacionComunidad").eq("idPublicacionComunidad", comentario.idPublicacionComunidad).execute()
            
            print(existePublicacion)
            if not existePublicacion.data:
                raise HTTPException(status_code=404, detail="La publicación no está disponible")
            
            response = supabase.table("ComentariosPublicaciones").insert(comentario.model_dump(mode="json")).execute()

            return {"message": "Comentario agregado correctamente", "data": response.data}
        
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error en el servidor al crear comentario {str(e)}", )
            print(e)


    async def responder_comentario(comentario: ComentarioPublicacionDto):
        try:
            existeComentario = supabase.table("ComentariosPublicaciones").select("idComentario")\
                .eq("idComentario", comentario.idComentarioPadre).execute()
            
            if not existeComentario.data:
                raise HTTPException(status_code=404, detail="El comentario no existe")
            
            response = supabase.table("ComentariosPublicaciones")\
                .insert(comentario.model_dump(mode="json")).execute()
            
            return {"message": "Respuesta agregada correctamente", "data": response.data}
        
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error en el servidor al agregar respuesta {str(e)}")



    