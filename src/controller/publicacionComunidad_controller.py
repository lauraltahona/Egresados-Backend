from src.service.publicacionComunidad_service import PublicacionComunidadService
from src.modelDto.publicacionComunidad_dto import PublicacionComunidadDto
from fastapi import APIRouter

publicacion_comunidad_router = APIRouter(tags=["Publicación Comunidad"])

@publicacion_comunidad_router.post("/publicacion-comunidad")
async def crear_publicacion_comunidad(publicacion_dto: PublicacionComunidadDto):
    return await PublicacionComunidadService.crear_publicacion_comunidad(publicacion_dto)