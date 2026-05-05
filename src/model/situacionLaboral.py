from pydantic import BaseModel, Field, model_validator
from datetime import date
from decimal import Decimal
import src.enum.situacionLaboral_enum as Enum

class SituacionLaboral(BaseModel):
    idSituacionLaboral: int
    estaEmpleado: bool
    empresaActual: str | None = Field(default=None, min_length=3, max_length=150,pattern=r"^[0-9A-Za-zñÑáéíóúÁÉÍÓÚ\s\.]+$")
    cargoActual: str | None = Field(default=None,min_length=3,max_length=150,pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    sectorEmpresa: Enum.SectorEmpresa | None = None
    sectorEmpresaOtro: str | None = Field(default=None,min_length=3,max_length=100,pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    tipoContrato: Enum.TipoContrato | None = None
    salarioActual: Decimal | None = Field(default=None)
    fechaIngreso: date | None = None
    idEgresado: int = Field(gt=0)

    