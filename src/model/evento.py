from pydantic import BaseModel, Field, HttpUrl
from datetime import date
import src.enum.evento_enum as Enum

class Evento(BaseModel):
    idEvento: int
    nombreEvento: str = Field(min_length=5, max_length=100, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    tipoEvento: Enum.TipoEvento
    horaEvento: date
    fechaEvento: date
    descripcionEvento: str = Field(min_length=10, max_length=500, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    lugarEvento: str = Field(min_length=3, max_length=150, pattern=r"^[0-9A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    modalidadEvento: Enum.ModalidadEvento
    estadoEvento: Enum.EstadoEvento
    organizadorEvento: str = Field(min_length=3, max_length=150, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    urlTransmision: HttpUrl
