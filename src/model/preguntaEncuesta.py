from enum import Enum
from pydantic import BaseModel, Field, validator


class TipoPregunta(str, Enum):
    SELECCION_UNICA = "Selección única"
    TEXTO_LIBRE = "Texto libre"


class PreguntaEncuesta(BaseModel):
    idPregunta: int
    textoPregunta: str = Field(min_length=5, max_length=300, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ0-9\s,.!?¿¡:;()\-\"\'@#]+$")
    tipoPregunta: TipoPregunta
    esFija: bool
    obligatoria: bool
    ordenPregunta: int = Field(gt=0)
    idEncuesta: int = Field(gt=0)