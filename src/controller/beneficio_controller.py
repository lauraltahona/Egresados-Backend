from src.model.beneficio import Beneficio
from src.service.beneficio_crud import BeneficioService
from fastapi import APIRouter

beneficio_router = APIRouter(tags=["Beneficio"])

@beneficio_router.post("/crear-beneficio")
def crear_beneficio_endpoint(beneficio: Beneficio):
    return BeneficioService.crear_beneficio(beneficio.model_dump())

@beneficio_router.get("/beneficios")
def leer_beneficios_endpoint():
    return BeneficioService.leer_beneficios()

@beneficio_router.get("/beneficio/{id_beneficio}")
def leer_beneficio_endpoint(id_beneficio: int):
    return BeneficioService.leer_beneficio_por_id(id_beneficio)

@beneficio_router.put("/actualizar-beneficio/{id_beneficio}")
def actualizar_beneficio_endpoint(id_beneficio: int, beneficio: Beneficio):
    return BeneficioService.actualizar_beneficio(id_beneficio, beneficio.model_dump())

@beneficio_router.delete("/eliminar-beneficio/{id_beneficio}")
def eliminar_beneficio_endpoint(id_beneficio: int):
    return BeneficioService.eliminar_beneficio(id_beneficio)