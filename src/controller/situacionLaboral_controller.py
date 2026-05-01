from src.service.situacionLaboral_crud import SituacionLaboralService
from src.modelDto.situacionLaboral_dto import SituacionLaboralDto
from fastapi import APIRouter

situacion_router = APIRouter(tags=["Situación Laboral"])

@situacion_router.post("/situacion")
async def crear_situacion_laboral(situacion: SituacionLaboralDto):
    return await SituacionLaboralService.crear_situacion_laboral(situacion)
      

@situacion_router.get("/situacion-laboral/{idEgresado}")
async def obtener_situacion_laboral_por_egresado(idEgresado: int):
    return await SituacionLaboralService.obtener_situacion_laboral_por_egresado(idEgresado)
    
    
@situacion_router.put("/situacion-laboral/actualizar/{idSituacion}")
async def actualizar_situacion_laboral(idSituacion: int, situacion: SituacionLaboralDto):
    return await SituacionLaboralService.actualizar_situacion_laboral(idSituacion, situacion)