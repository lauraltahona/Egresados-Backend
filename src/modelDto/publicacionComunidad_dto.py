from datetime import date
from pydantic import BaseModel, Field, HttpUrl
from typing import Optional
from src.enum.publicacionComunidad_enum import TipoPublicacion

class PublicacionComunidadDto(BaseModel):

    idComunidad: int = Field(..., gt=0)
    idEgresado: int = Field(..., gt=0)
    tituloPublicacion: str = Field(min_length=5, max_lenght=100, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ0-9\s]+$")
    contenidoPublicacion: str = Field(min_length=5, max_lenght=2000, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ0-9\s]+$")
    tipoPublicacion: TipoPublicacion | None = None
    fechaPublicacion: date
    urlImagen: Optional[HttpUrl] | None = None
