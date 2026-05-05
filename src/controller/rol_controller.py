from src.modelDto.rol_dto import rolDto
from src.service.rol_crud import RolService
from fastapi import APIRouter

rol_router = APIRouter(tags=["Rol"])

@rol_router.post("/crear-rol")
async def crear_rol_endpoint(rol: rolDto):
    return RolService.crear_rol(rol.model_dump())

@rol_router.get("/roles")
async def leer_roles_endpoint():
    return RolService.leer_roles()

@rol_router.put("/actualizar-rol/{id_rol}")
async def actualizar_rol_endpoint(id_rol: int, rol: rolDto):
    return RolService.actualizar_rol(id_rol, rol.model_dump())


@rol_router.delete("/eliminar-rol/{id_rol}")
async def eliminar_rol_endpoint(id_rol: int):
    return RolService.eliminar_rol(id_rol)