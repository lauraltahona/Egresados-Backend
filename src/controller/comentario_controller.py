from fastapi import APIRouter
from src.service.comentario_service import ComentarioPublicacionService
from src.modelDto.comentario_dto import ComentarioPublicacionDto

comentario_router = APIRouter(prefix="/comentario", tags=["Comentarios Publicaciones"])

@comentario_router.post("/")
async def crear_comentario(comentario: ComentarioPublicacionDto):
    return await ComentarioPublicacionService.crear_comentario(comentario)

@comentario_router.post("/responder")
async def responder_comentario(comentario: ComentarioPublicacionDto):
    return await ComentarioPublicacionService.responder_comentario(comentario)