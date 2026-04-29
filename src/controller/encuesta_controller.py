from src.model.encuesta import Encuesta
from src.service.encuesta_crud import EncuestaService
from fastapi import APIRouter

encuesta_router = APIRouter(tags=["Encuesta"])

@encuesta_router.post("/crear-encuesta")
def crear_encuesta_endpoint(encuesta: Encuesta):
    return EncuestaService.crear_encuesta(encuesta.model_dump())

@encuesta_router.get("/encuestas")
def leer_encuestas_endpoint():
    return EncuestaService.leer_encuestas()

@encuesta_router.get("/encuesta/{id_encuesta}")
def leer_encuesta_endpoint(id_encuesta: int):
    return EncuestaService.leer_encuesta_por_id(id_encuesta)

@encuesta_router.put("/actualizar-encuesta/{id_encuesta}")
def actualizar_encuesta_endpoint(id_encuesta: int, encuesta: Encuesta):
    return EncuestaService.actualizar_encuesta(id_encuesta, encuesta.model_dump())

@encuesta_router.delete("/eliminar-encuesta/{id_encuesta}")
def eliminar_encuesta_endpoint(id_encuesta: int):
    return EncuestaService.eliminar_encuesta(id_encuesta)