from datetime import date
from decimal import Decimal
from pydantic import BaseModel, Field, EmailStr
import src.enum.ofertaLaboral_enum as Enum

class OfertaLaboral(BaseModel):
    idOferta: int
    tituloOferta: str = Field(min_length=5, max_length=150, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ0-9\s\-\.]+$")
    nombreEmpresa: str = Field(min_length=3, max_length=150, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ0-9\s\-\.&]+$")
    descripcionOferta: str = Field(min_length=10, max_length=1000, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ0-9\s,.!?¿¡:;()\-\"\'\+@#]+$")
    salarioOfrecido: Decimal = Field(ge=0)
    ciudadOferta: str = Field(default=None, min_length=3, max_length=100, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    paisOferta: Enum.PaisOferta
    fechaPublicacion: date
    modalidadOferta: Enum.ModalidadOferta
    tipoContrato: Enum.TipoContrato
    jornadaLaboral: Enum.JornadaLaboral
    nivelExperiencia: Enum.NivelExperiencia
    nivelEstudios: Enum.NivelEstudios
    correoContacto: EmailStr = Field(min_length=6, max_length=150)