from datetime import date
from typing import Optional
from pydantic import BaseModel, Field
from src.enum.aplicacionOferta_enum import EstadoAplicacion


class AplicacionOfertaDto(BaseModel):
    idEgresado: int = Field(..., gt=0)
    idOferta: int = Field(..., gt=0)
    cartaPresentacion: Optional[str] = Field(default=None, min_length=50, max_length=3000, pattern=r"^[0-9A-Za-zñÑáéíóúÁÉÍÓÚ%.,:;()+\-\s]+$")
    rutaHojaVida: Optional[str] = Field(default=None, min_length=5, max_length=300)


class AplicacionOfertaEstadoDto(BaseModel):
    estadoAplicacion: EstadoAplicacion