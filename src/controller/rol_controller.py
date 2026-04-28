from src.model.rol import rol
from src.service.rol_crud import RolService
from fastapi import APIRouter

rol_router = APIRouter(tags=["Rol"])

@rol_router.post("/crear-rol")
async def crear_rol_endpoint(rol: rol):
    return await RolService.crear_rol(rol.model_dump())

@rol_router.get("/roles")
async def leer_roles_endpoint():
    return await RolService.leer_roles()