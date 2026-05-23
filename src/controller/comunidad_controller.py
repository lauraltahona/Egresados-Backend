from src.service.comunidad_service import ComunidadService
from fastapi import APIRouter
from src.modelDto.comunidad_dto import ComunidadDto, ComunidadUpdateDto

comunidad_router = APIRouter(prefix="/comunidades", tags=["Comunidades"])


@comunidad_router.post("/crear-comunidad/{idEgresado}")
async def crear_comunidad(comunidad_dto: ComunidadDto, idEgresado: int):
    return await ComunidadService.crear_comunidad(comunidad_dto, idEgresado)

@comunidad_router.post("/unirse-comunidad/{idComunidad}/{idEgresado}")
async def unirse_comunidad(idComunidad: int, idEgresado: int):
    return await ComunidadService.unirse_comunidad(idComunidad, idEgresado)

@comunidad_router.get("/obtener-comunidades")
async def obtener_comunidades(
    idComunidad: int | None = None,
    nombreComunidad: str | None = None,
    tipoComunidad: str | None = None
):
    return await ComunidadService.get_comunidades(idComunidad, nombreComunidad, tipoComunidad)

@comunidad_router.put("/actualizar-comunidad/{idComunidad}")
async def actualizar_comunidad(idComunidad: int, comunidad_dto: ComunidadUpdateDto):
    return await ComunidadService.actualizar_comunidad(idComunidad, comunidad_dto)

@comunidad_router.delete("/eliminar-comunidad/{idComunidad}")
async def eliminar_comunidad(idComunidad: int):
    return await ComunidadService.eliminar_comunidad(idComunidad)
