from src.model.rol import rol
from src.service.rol_service.rol_crud import RolService
from fastapi import APIRouter

rol_router = APIRouter()

@rol_router.post("/crear-rol")
def crear_rol_endpoint(rol: rol):
    return RolService.crear_rol(rol.model_dump())

@rol_router.get("/roles")
def leer_roles_endpoint():
    return RolService.leer_roles()

@rol_router.put("/actualizar-rol/{id_rol}")
def actualizar_rol_endpoint(id_rol: int, rol: rol):
    return RolService.actualizar_rol(id_rol, rol.model_dump())


@rol_router.delete("/eliminar-rol/{id_rol}")
def eliminar_rol_endpoint(id_rol: int):
    return RolService.eliminar_rol(id_rol)
