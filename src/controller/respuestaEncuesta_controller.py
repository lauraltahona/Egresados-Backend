from src.model.respuesta_encuesta import respuestaEncuesta
from src.service.respuesta_encuesta_service.respuesta_encuesta_crud import RespuestaEncuestaService
from fastapi import APIRouter

respuesta_encuesta_router = APIRouter()

@respuesta_encuesta_router.post("/crear-respuesta-encuesta")
def crear_respuesta_endpoint(respuesta: respuestaEncuesta):
    return RespuestaEncuestaService.crear_respuesta(respuesta.model_dump())

@respuesta_encuesta_router.get("/respuestas-encuestas")
def leer_respuestas_endpoint():
    return RespuestaEncuestaService.leer_respuestas()

@respuesta_encuesta_router.get("/respuesta-encuesta/{id_respuesta}")
def leer_respuesta_endpoint(id_respuesta: int):
    return RespuestaEncuestaService.leer_respuesta_por_id(id_respuesta)

@respuesta_encuesta_router.get("/respuestas-encuesta/{id_encuesta}")
def leer_respuestas_por_encuesta_endpoint(id_encuesta: int):
    return RespuestaEncuestaService.leer_respuestas_por_encuesta(id_encuesta)

@respuesta_encuesta_router.get("/respuestas-egresado/{id_egresado}")
def leer_respuestas_por_egresado_endpoint(id_egresado: int):
    return RespuestaEncuestaService.leer_respuestas_por_egresado(id_egresado)

@respuesta_encuesta_router.put("/actualizar-respuesta-encuesta/{id_respuesta}")
def actualizar_respuesta_endpoint(id_respuesta: int, respuesta: respuestaEncuesta):
    return RespuestaEncuestaService.actualizar_respuesta(id_respuesta, respuesta.model_dump())

@respuesta_encuesta_router.delete("/eliminar-respuesta-encuesta/{id_respuesta}")
def eliminar_respuesta_endpoint(id_respuesta: int):
    return RespuestaEncuestaService.eliminar_respuesta(id_respuesta)