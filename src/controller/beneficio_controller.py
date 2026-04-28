from src.model.beneficio import Beneficio
from src.service.beneficio_crud import BeneficioService
from fastapi import APIRouter

beneficio_router = APIRouter(
    prefix="/beneficios",
    tags=["Beneficios"]
)

@beneficio_router.post("/")
def crear_beneficio_endpoint(beneficio: Beneficio):
    return BeneficioService.crear_beneficio(beneficio.model_dump())

@beneficio_router.get("/")
def leer_beneficios_endpoint():
    return BeneficioService.leer_beneficios()