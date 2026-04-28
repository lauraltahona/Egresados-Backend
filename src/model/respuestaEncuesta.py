from enum import Enum
from datetime import date
from typing import Optional
from pydantic import BaseModel, Field, validator


class RespuestaEncuesta(BaseModel):
    respuestaTexto: Optional[str] = Field(default=None, min_length=1, max_length=500,
        pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ0-9\s,.!?¿¡:;()\-\"\'@#]+$")
    respuestaOpcion: Optional[str] = Field(default=None)
    fechaRespuesta: date
    idPregunta: int = Field(gt=0)
    idEgresado: int = Field(gt=0)