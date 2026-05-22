from datetime import date
from pydantic import BaseModel, Field
from typing import Optional
from src.enum.comunidad_enum import TipoComunidad

class ComunidadDto(BaseModel):
    nombreComunidad: str = Field(min_length=5, max_length=100, pattern=r"^[A-Za-záéíóúñÁÉÍÓÚÑ0-9\s.,()-]+$")
    descripcionComunidad: str | None = Field(None, min_length=10, max_length=500, pattern=r"^[A-Za-záéíóúñÁÉÍÓÚÑ0-9\s.,()-]+$") 
    tipoComunidad: TipoComunidad | None = None
    fechaCreacion: Optional[date] = None
    estado: Optional[bool] = True

class ComunidadUpdateDto(BaseModel):
    nombreComunidad: Optional[str] | None= Field(default=None, min_length=5, max_length=100, pattern=r"^[A-Za-záéíóúñÁÉÍÓÚÑ0-9\s.,()-]+$") 
    descripcionComunidad: Optional[str] | None = Field(default=None, min_length=10, max_length=500, pattern=r"^[A-Za-záéíóúñÁÉÍÓÚÑ0-9\s.,()-]+$") 
    tipoComunidad: TipoComunidad | None = None
    fechaCreacion: Optional[date] | None = None
    estado: Optional[bool] | None = True



