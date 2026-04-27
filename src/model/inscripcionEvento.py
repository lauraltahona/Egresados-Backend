from pydantic import BaseModel
from datetime import date
from enum import Enum

class EstadoAsistencia(str, Enum):
    ASISTIO = "Asistió"
    NO_ASISTIO = "No asistió"

class InscripcionEvento(BaseModel):
    idInscripcion: int
    fechaInscripcion: date
    estadoAsistencia: EstadoAsistencia
    idEgresado: int
    idEvento: int