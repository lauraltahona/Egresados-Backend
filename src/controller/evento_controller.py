from fastapi import APIRouter
from src.service.evento_crud import EventoService
from src.modelDto.evento_dto import  EventoDto, EventoUpdateDto, EventoEstadoDto
import src.enum.evento_enum as Enum

evento_router = APIRouter(prefix="/evento", tags=["Evento"])

@evento_router.post("/crear")
async def crear_evento(evento: EventoDto):
    return await EventoService.crear_evento(evento.model_dump(mode='json'))

@evento_router.get("/leer")
def leer_eventos():
    return EventoService.leer_eventos()

@evento_router.get("/leer/{estadoEvento}")
def leer_eventos_por_estado(estadoEvento: Enum.EstadoEvento):
    return EventoService.leer_eventos_por_estado(estadoEvento)

@evento_router.get("/{idEvento}")
def obtener_evento(idEvento: int):
    return EventoService.leer_evento_por_id(idEvento)

@evento_router.put("/actualizar/{idEvento}")
def actualizar_evento(idEvento: int, evento: EventoUpdateDto):
    datos = {k: v for k, v in evento.model_dump(mode='json').items() if v is not None}
    return EventoService.actualizar_evento(idEvento, datos)

@evento_router.patch("/estado/{idEvento}")
def actualizar_estado(idEvento: int, body: EventoEstadoDto):
    return EventoService.actualizar_estado_evento(idEvento, body.estadoEvento)

@evento_router.delete("/eliminar/{idEvento}")
def eliminar_evento(idEvento: int):
    return EventoService.eliminar_evento(idEvento)