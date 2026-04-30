from src.service.situacionLaboral_crud import SituacionLaboral_Service
from src.modelDto.situacionLaboral_dto import SituacionLaboralDto
from fastapi import APIRouter

situacion_router = APIRouter(tags=["Situación Laboral"])

@situacion_router.post("/situacion-laboral")
def crear_situacion_laboral(situacion: SituacionLaboralDto):
    try:
        response = SituacionLaboral_Service.crear_situacion_laboral(situacion)
        return response
    except Exception as e:
        return {"error": str(e)}
    
@situacion_router.get("/situacion-laboral/{idEgresado}")
def obtener_situacion_laboral_por_egresado(idEgresado: int):
    try:
        response = SituacionLaboral_Service.obtener_situacion_laboral_por_egresado(idEgresado)
        return response
    except Exception as e:
        return {"error": str(e)}
    
@situacion_router.put("/situacion-laboral/actualizar/{idSituacion}")
def actualizar_situacion_laboral(idSituacion: int, situacion: SituacionLaboralDto):
    try:
        response = SituacionLaboral_Service.actualizar_situacion_laboral(idSituacion, situacion)
        return response
    except Exception as e:
        return {"error": str(e)}