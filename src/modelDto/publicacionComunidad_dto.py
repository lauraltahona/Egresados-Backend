from datetime import date
from pydantic import BaseModel, Field, HttpUrl, model_validator
from typing import Optional
from src.enum.publicacionComunidad_enum import TipoPublicacion

class PublicacionComunidadDto(BaseModel):

    idComunidad: int = Field(..., gt=0)
    idEgresado: int = Field(..., gt=0)
    tituloPublicacion: Optional[str] = Field(None, min_length=5, max_lenght=100, pattern=r"^[0-9A-Za-zñÑáéíóúÁÉÍÓÚ%.,:;()+\-\s]+$")
    contenidoPublicacion: Optional[str] | None = Field(None, min_length=5, max_lenght=2000, pattern=r"^[0-9A-Za-zñÑáéíóúÁÉÍÓÚ%.,:;()+\-\s]+$")
    tipoPublicacion: TipoPublicacion | None = None
    fechaPublicacion: date
    urlImagen: Optional[HttpUrl] | None = None

    @model_validator(mode="after")
    def validar_fecha(self):
        if self.fechaPublicacion > date.today():
            raise ValueError("La fecha de publicación no puede ser futura")
        return self

    @model_validator(mode="after")
    def validar_contenido(self):
        if not self.tituloPublicacion and not self.contenidoPublicacion and not self.urlImagen:
            raise ValueError("Debe proporcionar al menos un título, contenido o imagen para la publicación")
        return self
    