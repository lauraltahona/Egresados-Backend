from src.service.publicacionComunidad_service import PublicacionComunidadService
from src.modelDto.publicacionComunidad_dto import PublicacionComunidadDto
from src.service.moderador_service import ModeracionService
from fastapi import APIRouter

publicacion_comunidad_router = APIRouter(prefix="/publicacion-comunidad", tags=["Publicación Comunidad"])

@publicacion_comunidad_router.post("/")
async def crear_publicacion_comunidad(publicacion_dto: PublicacionComunidadDto):
    validacion = ModeracionService.validar_contenido(publicacion_dto.contenidoPublicacion)

    response = await PublicacionComunidadService.crear_publicacion_comunidad(publicacion_dto)

    return response

@publicacion_comunidad_router.get("/publicaciones/{idComunidad}")
async def get_publicaciones_comunidad(idComunidad: int):
    return await PublicacionComunidadService.get_publicaciones_comunidad(idComunidad)

@publicacion_comunidad_router.delete("/{idPublicacion}")
async def eliminar_publicacion_comunidad(idPublicacion: int, idEgresado: int):
    return await PublicacionComunidadService.eliminar_publicacion_comunidad(idPublicacion, idEgresado)