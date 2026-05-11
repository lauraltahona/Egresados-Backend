from pydantic import BaseModel, Field, model_validator
from datetime import date

class InscripcionEventoDto(BaseModel):
    idEgresado: int = Field(gt=0)
    idEvento: int = Field(gt=0)

class ActualizarAsistenciaDto(BaseModel):
    estadoAsistencia: bool