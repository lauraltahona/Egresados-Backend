from fastapi import APIRouter
from src.service.facultad_crud import FacultadService
from src.modelDto.facultad_dto import  FacultadDto

facultad_router = APIRouter(tags=["Facultad"])

@facultad_router.get("/facultades")
async def leer_facultades_endpoint():
    return await FacultadService.leer_facultades()

@facultad_router.post("/crear-facultad")
async def crear_facultad_endpoint(facultad: FacultadDto):
    return await FacultadService.crear_facultad(facultad.model_dump())