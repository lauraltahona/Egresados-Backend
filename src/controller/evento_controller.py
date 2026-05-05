from fastapi import APIRouter
from src.service.evento_crud import EventoService
from src.modelDto.evento_dto import  EventoDto
import src.enum.evento_enum as Enum

evento_router = APIRouter(prefix="/evento", tags=["Evento"])

@evento_router.post("/crear")
async def crear_evento(evento: EventoDto):
    return EventoService.crear_evento(evento.model_dump())

@evento_router.get("/leer")
def leer_eventos_endpoint():
    return EventoService.leer_eventos()

@evento_router.get("/leer/{estadoEvento}")
def leer_eventos_endpoint(estadoEvento: Enum.EstadoEvento):
    return EventoService.leer_eventos(estadoEvento)