from pydantic import BaseModel
from datetime import date
import src.enum.inscripcionEvento_enum as Enum

class InscripcionEvento(BaseModel):
    idInscripcion: int
    fechaInscripcion: date
    estadoAsistencia: Enum.EstadoAsistencia
    idEgresado: int
    idEvento: int