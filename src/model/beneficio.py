from pydantic import BaseModel, Field, EmailStr, field_validator, model_validator
from datetime import date
import src.enum.beneficio_enum as Enum

class Beneficio(BaseModel):
    idBeneficio: int
    nombreBeneficio: str = Field(min_length=3, max_length=150, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    tipoBeneficio: Enum.TipoBeneficio
    tipoBeneficioOtro: str | None = Field(default=None,min_length=3,max_length=100,pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    descripcionBeneficio: str = Field(min_length=10, max_length=500,pattern=r"^[0-9A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    objetoBeneficio: str = Field(min_length=10, max_length=300, pattern=r"^[0-9A-Za-zñÑáéíóúÁÉÍÓÚ\s%]+$")
    empresaConvenio: str = Field(min_length=3, max_length=150, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    contactoEmpresa: str = Field(min_length=3,max_length=150,pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    correoEmpresa: EmailStr
    telefonoEmpresa: str = Field(pattern=r"^\d{10}$")
    fechaInicioConvenio: date
    fechaVencimientoConvenio: date
    estadoConvenio: Enum.EstadoConvenio
    documentoConvenio: str | None = Field(default=None,min_length=5,max_length=300)