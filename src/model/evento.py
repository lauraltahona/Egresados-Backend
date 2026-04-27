from pydantic import BaseModel, Field, HttpUrl
from enum import Enum
from datetime import date

class TipoEvento(str, Enum):
    CULTURAL = "Cultural"
    DEPORTIVO = "Deportivo"

class ModalidadEvento(str, Enum):
    PRESENCIAL = "Presencial"
    VIRTUAL = "Virtual"
    HIBRIDO = "Híbrido"

class EstadoEvento(str, Enum):
    PROGRAMADO = "Programado"
    EN_CURSO = "En curso"
    CANCELADO = "Cancelado"

class Evento(BaseModel):
    idEvento: int
    nombreEvento: str = Field(min_length=5, max_length=100, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    tipoEvento: TipoEvento
    horaEvento: date
    fechaEvento: date
    descripcionEvento: str = Field(min_length=10, max_length=500, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    lugarEvento: str = Field(min_length=3, max_length=150, pattern=r"^[0-9A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    modalidadEvento: ModalidadEvento
    estadoEvento: EstadoEvento
    organizadorEvento: str = Field(min_length=3, max_length=150, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    urlTransmision: HttpUrl
