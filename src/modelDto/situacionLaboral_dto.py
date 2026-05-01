from pydantic import BaseModel, Field, model_validator
from src.model.situacionLaboral import SectorEmpresa, TipoContrato
from enum import Enum
from datetime import date
from decimal import Decimal


class SituacionLaboralDto(BaseModel):
    estaEmpleado: bool
    empresaActual: str | None = Field(default=None, min_length=3, max_length=150,pattern=r"^[0-9A-Za-zñÑáéíóúÁÉÍÓÚ\s\.]+$")
    cargoActual: str | None = Field(default=None,min_length=3,max_length=150,pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    sectorEmpresa: SectorEmpresa | None = None
    sectorEmpresaOtro: str | None = Field(default=None,min_length=3,max_length=100,pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    tipoContrato: TipoContrato | None = None
    salarioActual: Decimal | None = Field(default=None, gt=0)
    fechaIngreso: date | None = None
    idEgresado: int | None = Field(default=None, gt=0)

    @model_validator(mode="after")
    def validar_empresa(self):
        if self.estaEmpleado:
            if not self.empresaActual:
                raise ValueError("Debe especificar la empresa")
        return self
    

    @model_validator(mode="after")
    def validar_fecha(self):
        if self.fechaIngreso and self.fechaIngreso > date.today():
            raise ValueError("La fecha de ingreso no puede ser futura")
        return self
    
    @model_validator(mode="after")
    def validar_salario(self):
        if self.estaEmpleado:
            if not self.salarioActual:
                raise ValueError("Obligatorio poner salario si está empleado")
        return self
    