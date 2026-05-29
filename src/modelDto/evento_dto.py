from pydantic import BaseModel, Field, HttpUrl, model_validator
from datetime import date, time
from typing import Optional
import src.enum.evento_enum as Enum

class EventoDto(BaseModel):
    nombreEvento: str = Field(min_length=5, max_length=100, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    tipoEvento: Enum.TipoEvento
    horaEvento: time
    fechaEvento: date
    descripcionEvento: str = Field(min_length=10, max_length=500, pattern=r"^[0-9A-Za-zñÑáéíóúÁÉÍÓÚ%.,:;()+\-\s]+$")
    lugarEvento: str = Field(min_length=3, max_length=150, pattern=r"^[0-9A-Za-zñÑáéíóúÁÉÍÓÚ%.,:;()+\-\s]+$")
    modalidadEvento: Enum.ModalidadEvento
    organizadorEvento: str = Field(min_length=3, max_length=150, pattern=r"^[0-9A-Za-zñÑáéíóúÁÉÍÓÚ%.,:;()+\-\s]+$")
    urlTransmision: Optional[HttpUrl] = None
    
    @model_validator(mode="after")
    def validar_url_transmision(self):
        if self.modalidadEvento in (Enum.ModalidadEvento.VIRTUAL, Enum.ModalidadEvento.HIBRIDO):
            if not self.urlTransmision:
                raise ValueError("Debe proporcionar una URL de transmisión para eventos virtuales o híbridos")
        return self

    @model_validator(mode="after")
    def validar_fecha(self):
        if self.fechaEvento < date.today():
            raise ValueError("La fecha del evento no puede ser menor a la actual")
        return self
    
class EventoUpdateDto(BaseModel):
    nombreEvento: Optional[str] = Field(default=None, min_length=5, max_length=100, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    tipoEvento: Optional[Enum.TipoEvento] = None
    fechaEvento: Optional[date] = None
    horaEvento: Optional[time] = None
    descripcionEvento: Optional[str] = Field(default=None, min_length=10, max_length=500)
    lugarEvento: Optional[str] = Field(default=None, min_length=3, max_length=150, pattern=r"^[0-9A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    modalidadEvento: Optional[Enum.ModalidadEvento] = None
    organizadorEvento: Optional[str] = Field(default=None, min_length=3, max_length=150, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    urlTransmision: Optional[HttpUrl] = None

    @model_validator(mode="after")
    def validar_fecha(self):
        if self.fechaEvento and self.fechaEvento < date.today():
            raise ValueError("La fecha del evento no puede ser menor a la actual")
        return self


class EventoEstadoDto(BaseModel):
    estadoEvento: Enum.EstadoEvento