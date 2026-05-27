from src.modelDto.beneficio_dto import BeneficioDto, BeneficioDtoUpdate
from src.service.beneficio_crud import BeneficioService
from fastapi import APIRouter

beneficio_router = APIRouter(prefix="/beneficio", tags=["Beneficio"])

@beneficio_router.post("/crear")
async def crear_beneficio_endpoint(beneficio: BeneficioDto):
    return await BeneficioService.crear_beneficio(beneficio)

@beneficio_router.get("/")
async def leer_beneficios_endpoint():
    return await BeneficioService.leer_beneficios()

@beneficio_router.get("/{id_beneficio}")
async def leer_beneficio_endpoint(id_beneficio: int):
    return await BeneficioService.leer_beneficio_por_id(id_beneficio)

@beneficio_router.patch("/actualizar/{id_beneficio}")
async def actualizar_beneficio_endpoint(id_beneficio: int, beneficio: BeneficioDtoUpdate):
    return await BeneficioService.actualizar_beneficio(id_beneficio, beneficio.model_dump())

@beneficio_router.delete("/eliminar/{id_beneficio}")
async def eliminar_beneficio_endpoint(id_beneficio: int):
    return await BeneficioService.eliminar_beneficio(id_beneficio)