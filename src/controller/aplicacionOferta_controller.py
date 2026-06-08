from fastapi import APIRouter
from src.service.aplicacionOferta_service import AplicacionOfertaService
from src.modelDto.aplicacionOferta_dto import AplicacionOfertaDto, AplicacionOfertaEstadoDto

aplicacion_router = APIRouter(prefix="/aplicaciones", tags=["Aplicaciones Ofertas Laborales"])


@aplicacion_router.post("/postular")
async def postular_egresado(aplicacion: AplicacionOfertaDto):
    return await AplicacionOfertaService.postular_egresado(aplicacion)


@aplicacion_router.get("/oferta/{idOferta}")
async def listar_egresados_por_oferta(idOferta: int):
    return await AplicacionOfertaService.listar_egresados_por_oferta(idOferta)


@aplicacion_router.delete("/{idAplicacion}/egresado/{idEgresado}")
async def eliminar_postulacion(idAplicacion: int, idEgresado: int):
    return await AplicacionOfertaService.eliminar_postulacion(idAplicacion, idEgresado)


@aplicacion_router.patch("/estado/{idAplicacion}")
async def actualizar_estado_aplicacion(idAplicacion: int, body: AplicacionOfertaEstadoDto):
    return await AplicacionOfertaService.actualizar_estado_aplicacion(idAplicacion, body.estadoAplicacion)