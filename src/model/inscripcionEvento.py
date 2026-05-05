from pydantic import BaseModel
from datetime import date

class InscripcionEvento(BaseModel):
    idInscripcion: int
    fechaInscripcion: date
    estadoAsistencia: bool
    idEgresado: int
    idEvento: int