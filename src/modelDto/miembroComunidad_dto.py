from datetime import date
from pydantic import BaseModel, Field
from typing import Optional
from src.enum.miembroComunidad_enum import RolMiembro


class MiembroComunidadDto(BaseModel):
    rolMiembro: RolMiembro
    estadoMiembro: Optional[bool]
    fechaIngreso: Optional[date]
    fechaSalida: Optional[date] | None = None
    idEgresado: int = Field(..., gt=0)
    idComunidad: int = Field(..., gt=0)