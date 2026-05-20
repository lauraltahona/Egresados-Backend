from src.service.miembroComunidad_service import MiembroComunidadService
from fastapi import APIRouter, HTTPException
from src.modelDto.miembroComunidad_dto import MiembroComunidadDto

miembro_comunidad_router = APIRouter(prefix="/miembro-comunidad", tags=["Miembro Comunidad"])

@miembro_comunidad_router.post("/")
async def crear_miembro_comunidad(miembro_comunidad_dto: MiembroComunidadDto):
    return await MiembroComunidadService.crear_miembro_comunidad(miembro_comunidad_dto)


@miembro_comunidad_router.get("/comunidad/{idComunidad}")
async def obtener_miembros_comunidad(idComunidad: int):
    return await MiembroComunidadService.obtener_miembros_comunidad(idComunidad)

@miembro_comunidad_router.delete("/{idMiembro}")
async def eliminar_miembro_comunidad(idMiembro: int):
    return await MiembroComunidadService.eliminar_miembro_comunidad(idMiembro)