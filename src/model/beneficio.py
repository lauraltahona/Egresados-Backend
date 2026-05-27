from pydantic import BaseModel, Field, EmailStr, field_validator, model_validator
from datetime import date
import src.enum.beneficio_enum as Enum

class Beneficio(BaseModel):
    idBeneficio: int
    nombreBeneficio: str 
    tipoBeneficioOtro: str 
    descripcionBeneficio: str
    objetoBeneficio: str 
    empresaConvenio: str 
    contactoEmpresa: str 
    correoEmpresa: EmailStr
    telefonoEmpresa: str 
    fechaInicioConvenio: date
    fechaVencimientoConvenio: date
    estadoConvenio: Enum.EstadoConvenio
    documentoConvenio: str 