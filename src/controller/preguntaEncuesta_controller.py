from src.model.preguntaEncuesta import PreguntaEncuesta
from src.service.preguntaEncuesta_crud import PreguntaEncuestaService
from fastapi import APIRouter

pregunta_encuesta_router = APIRouter(tags=["Pregunta Encuesta"])

@pregunta_encuesta_router.post("/crear-pregunta-encuesta")
def crear_pregunta_endpoint(pregunta: PreguntaEncuesta):
    return PreguntaEncuestaService.crear_pregunta(pregunta.model_dump())

@pregunta_encuesta_router.get("/preguntas-encuestas")
def leer_preguntas_endpoint():
    return PreguntaEncuestaService.leer_preguntas()

@pregunta_encuesta_router.get("/pregunta-encuesta/{id_pregunta}")
def leer_pregunta_endpoint(id_pregunta: int):
    return PreguntaEncuestaService.leer_pregunta_por_id(id_pregunta)

@pregunta_encuesta_router.get("/preguntas-encuesta/{id_encuesta}")
def leer_preguntas_por_encuesta_endpoint(id_encuesta: int):
    return PreguntaEncuestaService.leer_preguntas_por_encuesta(id_encuesta)

@pregunta_encuesta_router.put("/actualizar-pregunta-encuesta/{id_pregunta}")
def actualizar_pregunta_endpoint(id_pregunta: int, pregunta: PreguntaEncuesta):
    return PreguntaEncuestaService.actualizar_pregunta(id_pregunta, pregunta.model_dump())

@pregunta_encuesta_router.delete("/eliminar-pregunta-encuesta/{id_pregunta}")
def eliminar_pregunta_endpoint(id_pregunta: int):
    return PreguntaEncuestaService.eliminar_pregunta(id_pregunta)