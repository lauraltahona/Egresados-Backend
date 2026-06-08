from datetime import date
from typing import Optional
from pydantic import BaseModel, Field
from src.enum.aplicacionOferta_enum import EstadoAplicacion


class AplicacionOferta(BaseModel):
    idAplicacion: int
    fechaAplicacion: date
    estadoAplicacion: Optional[EstadoAplicacion] = None
    cartaPresentacion: Optional[str] = Field(default=None, min_length=50, max_length=3000, pattern=r"^[0-9A-Za-zñÑáéíóúÁÉÍÓÚ%.,:;()+\-\s]+$")
    rutaHojaVida: Optional[str] = Field(default=None, min_length=5, max_length=300)
    fechaActualizacionEstado: Optional[date] = None
    idEgresado: Optional[int] = Field(default=None, gt=0)
    idOferta: Optional[int] = Field(default=None, gt=0)