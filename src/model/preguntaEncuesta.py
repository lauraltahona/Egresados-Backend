from pydantic import BaseModel, Field, validator
import src.enum.preguntaEncuesta_enum as Enum

class PreguntaEncuesta(BaseModel):
    idPregunta: int
    textoPregunta: str = Field(min_length=5, max_length=300, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ0-9\s,.!?¿¡:;()\-\"\'@#]+$")
    tipoPregunta: Enum.TipoPregunta
    esFija: bool
    obligatoria: bool
    ordenPregunta: int = Field(gt=0)
    idEncuesta: int = Field(gt=0)