from src.service.proyecto_crud import ProyectoService
from src.modelDto.proyecto_dto import ProyectoDto


from fastapi import APIRouter

proyecto_router = APIRouter(tags=["Proyecto"])

@proyecto_router.post("/crear-proyecto")
async def crear_proyecto_endpoint(proyecto: ProyectoDto):
    return await ProyectoService.crear_proyecto(proyecto.model_dump())

@proyecto_router.get("/proyectos")
async def obtener_proyectos_endpoint():
    return await ProyectoService.obtener_proyectos()