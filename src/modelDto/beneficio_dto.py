from pydantic import BaseModel, Field, EmailStr, field_validator, model_validator
from datetime import date
import src.enum.beneficio_enum as Enum

class BeneficioDto(BaseModel):
    nombreBeneficio: str = Field(min_length=3, max_length=150, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    tipoBeneficio: Enum.TipoBeneficio
    tipoBeneficioOtro: str | None = Field(default=None,min_length=3,max_length=100,pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    descripcionBeneficio: str | None = Field(None, min_length=10, max_length=500,pattern=r"^[0-9A-Za-zñÑáéíóúÁÉÍÓÚ\s.,;:%()\-]+$")
    objetoBeneficio: str | None = Field(None, min_length=10, max_length=300, pattern=r"^[0-9A-Za-zñÑáéíóúÁÉÍÓÚ\s%]+$")
    empresaConvenio: str | None = Field(None, min_length=3, max_length=150, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    contactoEmpresa: str | None = Field(None, min_length=3,max_length=150,pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    correoEmpresa: EmailStr | None = None
    telefonoEmpresa: str | None = Field(None, pattern=r"^\d{10}$")
    fechaInicioConvenio: date | None = None
    fechaVencimientoConvenio: date | None = None
    estadoConvenio: Enum.EstadoConvenio | None = None
    documentoConvenio: str | None = Field(default=None,min_length=5,max_length=300)

class BeneficioDtoUpdate(BaseModel):
    nombreBeneficio: str | None = Field(None, min_length=3, max_length=150, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    tipoBeneficio: Enum.TipoBeneficio | None = None
    tipoBeneficioOtro: str | None = Field(default=None,min_length=3,max_length=100,pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    descripcionBeneficio: str | None = Field(None, min_length=10, max_length=500,pattern=r"^[0-9A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    objetoBeneficio: str | None = Field(None, min_length=10, max_length=300, pattern=r"^[0-9A-Za-zñÑáéíóúÁÉÍÓÚ\s%]+$")
    empresaConvenio: str | None = Field(None, min_length=3, max_length=150, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    contactoEmpresa: str | None = Field(None, min_length=3,max_length=150,pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    correoEmpresa: EmailStr | None = None
    telefonoEmpresa: str | None = Field(None, pattern=r"^\d{10}$")
    fechaInicioConvenio: date | None = None
    fechaVencimientoConvenio: date | None = None
    estadoConvenio: Enum.EstadoConvenio | None = None
    documentoConvenio: str | None = Field(default=None,min_length=5,max_length=300)