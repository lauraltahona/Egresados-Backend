from src.service.egresado_crud import EgresadoService
from src.modelDto.egresado_dto import EgresadoDto
from fastapi import APIRouter

egresado_router = APIRouter(tags=["Egresados"])

@egresado_router.post("/egresados")
def crear_egresado(egresado: EgresadoDto):
    try:
        response = EgresadoService.crear_egresado(egresado)
        return response
    except Exception as e:
        return {"Error al crear el egresado": str(e)}