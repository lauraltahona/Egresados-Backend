from fastapi import APIRouter
from src.service.comentario_service import ComentarioPublicacionService
from src.modelDto.comentario_dto import ComentarioPublicacionDto
from src.service.moderador_service import ModeracionService

comentario_router = APIRouter(prefix="/comentario", tags=["Comentarios Publicaciones"])

@comentario_router.post("/")
async def crear_comentario(comentario: ComentarioPublicacionDto):
    validacion = await ModeracionService.validar_contenido(comentario.contenidoComentario)
    response = await ComentarioPublicacionService.crear_comentario(comentario)
    return response

@comentario_router.post("/responder/{idComentarioPadre}")
async def responder_comentario(idComentarioPadre: int, comentario: ComentarioPublicacionDto):
    validacion = await ModeracionService.validar_contenido(comentario.contenidoComentario)
    response = await ComentarioPublicacionService.responder_comentario(idComentarioPadre, comentario)
    return response