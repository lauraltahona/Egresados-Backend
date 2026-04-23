from src.model.rol import rol
import src.service.rol_service.rol_crud as rol_service
from fastapi import APIRouter

rol_router = APIRouter()

@rol_router.post("/crear-rol")
def crear_rol_endpoint(rol: rol):
    return rol_service.crear_rol(rol.model_dump())