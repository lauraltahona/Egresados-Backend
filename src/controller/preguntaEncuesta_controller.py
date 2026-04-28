from fastapi import APIRouter
from src.model.preguntaEncuesta import PreguntaEncuesta
from src.service.preguntaEncuesta_crud import PreguntaEncuestaService

preguntaEncuesta_router = APIRouter(
    prefix="/preguntas-encuesta",
    tags=["Preguntas Encuesta"]
)

@preguntaEncuesta_router.post("/")
def crear_pregunta_endpoint(pregunta: PreguntaEncuesta):
    return PreguntaEncuestaService.crear_pregunta(pregunta.model_dump())

@preguntaEncuesta_router.get("/")
def leer_preguntas_endpoint():
    return PreguntaEncuestaService.leer_preguntas()

@preguntaEncuesta_router.get("/{id_pregunta}")
def leer_pregunta_endpoint(id_pregunta: int):
    return PreguntaEncuestaService.leer_pregunta_por_id(id_pregunta)

@preguntaEncuesta_router.get("/encuesta/{id_encuesta}")
def leer_preguntas_por_encuesta_endpoint(id_encuesta: int):
    return PreguntaEncuestaService.leer_preguntas_por_encuesta(id_encuesta)

@preguntaEncuesta_router.put("/{id_pregunta}")
def actualizar_pregunta_endpoint(id_pregunta: int, pregunta: PreguntaEncuesta):
    return PreguntaEncuestaService.actualizar_pregunta(id_pregunta, pregunta.model_dump())

@preguntaEncuesta_router.delete("/{id_pregunta}")
def eliminar_pregunta_endpoint(id_pregunta: int):
    return PreguntaEncuestaService.eliminar_pregunta(id_pregunta)