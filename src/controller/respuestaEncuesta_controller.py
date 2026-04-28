from fastapi import APIRouter
from src.model.respuestaEncuesta import RespuestaEncuesta
from src.service.respuestaEncuesta_crud import RespuestaEncuestaService

respuestaEncuesta_router = APIRouter(
    prefix="/respuestas-encuesta",
    tags=["Respuestas Encuesta"]
)

@respuestaEncuesta_router.post("/")
def crear_respuesta_endpoint(respuesta: RespuestaEncuesta):
    return RespuestaEncuestaService.crear_respuesta(respuesta.model_dump())

@respuestaEncuesta_router.get("/")
def leer_respuestas_endpoint():
    return RespuestaEncuestaService.leer_respuestas()

@respuestaEncuesta_router.get("/{id_respuesta}")
def leer_respuesta_endpoint(id_respuesta: int):
    return RespuestaEncuestaService.leer_respuesta_por_id(id_respuesta)

@respuestaEncuesta_router.get("/encuesta/{id_encuesta}")
def leer_respuestas_por_encuesta_endpoint(id_encuesta: int):
    return RespuestaEncuestaService.leer_respuestas_por_encuesta(id_encuesta)

@respuestaEncuesta_router.get("/egresado/{id_egresado}")
def leer_respuestas_por_egresado_endpoint(id_egresado: int):
    return RespuestaEncuestaService.leer_respuestas_por_egresado(id_egresado)

@respuestaEncuesta_router.put("/{id_respuesta}")
def actualizar_respuesta_endpoint(id_respuesta: int, respuesta: RespuestaEncuesta):
    return RespuestaEncuestaService.actualizar_respuesta(id_respuesta, respuesta.model_dump())

@respuestaEncuesta_router.delete("/{id_respuesta}")
def eliminar_respuesta_endpoint(id_respuesta: int):
    return RespuestaEncuestaService.eliminar_respuesta(id_respuesta)