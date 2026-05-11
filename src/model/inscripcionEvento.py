from pydantic import BaseModel, Field
from datetime import date

class InscripcionEvento(BaseModel):
    idInscripcion: int
    fechaInscripcion: date
    estadoAsistencia: bool
    idEgresado: int = Field(gt=0)
    idEvento: int = Field(gt=0)