from pydantic import BaseModel, Field, model_validator
from enum import Enum
from datetime import date
from decimal import Decimal

class SectorEmpresa(str, Enum):
    TECNOLOGIA = "Tecnología"
    SALUD = "Salud"
    EDUCACION = "Educación"
    COMERCIO = "Comercio"
    INDUSTRIA = "Industria"
    GOBIERNO = "Gobierno"
    OTRO = "Otro"

class TipoContrato(str, Enum):
    TERMINO_FIJO = "Término fijo"
    TERMINO_INDEFINIDO = "Término indefinido"
    PRESTACION_SERVICIOS = "Prestación de servicios"
    POR_OBRA = "Por obra"

class SituacionLaboral(BaseModel):
    idSituacionLaboral: int
    estaEmpleado: bool
    empresaActual: str | None = Field(default=None, min_length=3, max_length=150,pattern=r"^[0-9A-Za-zñÑáéíóúÁÉÍÓÚ\s\.]+$")
    cargoActual: str | None = Field(default=None,min_length=3,max_length=150,pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    sectorEmpresa: SectorEmpresa | None = None
    sectorEmpresaOtro: str | None = Field(default=None,min_length=3,max_length=100,pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    tipoContrato: TipoContrato | None = None
    salarioActual: Decimal | None = Field(default=None)
    fechaIngreso: date | None = None
    idEgresado: int = Field(gt=0)

    