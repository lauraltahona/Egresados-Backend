from src.service.egresado_crud import EgresadoService
from src.modelDto.egresado_dto import EgresadoDto
from fastapi import APIRouter

egresado_router = APIRouter(tags=["Egresados"])

@egresado_router.post("/egresados")
async def crear_egresado(egresado: EgresadoDto):
    response = await EgresadoService.crear_egresado(egresado)
    return response

@egresado_router.get("/egresados")  
async def get_egresados():
    response = await EgresadoService.get_egresados()
    return response

@egresado_router.get("/egresados/{idEgresado}")
async def get_egresado_by_id(idEgresado: int):
    response = await EgresadoService.get_egresado_by_id(idEgresado)
    return response 