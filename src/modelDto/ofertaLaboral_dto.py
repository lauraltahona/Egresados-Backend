from src.model.ofertaLaboral import ModalidadOferta, TipoContrato, JornadaLaboral, NivelExperiencia, NivelEstudios, PaisOferta
from datetime import date
from decimal import Decimal
from pydantic import BaseModel, Field, EmailStr, model_validator, HttpUrl

class OfertaLaboralDTO(BaseModel):
    tituloOferta: str = Field(min_length=5, max_length=150, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ0-9\s\-\.]+$")
    nombreEmpresa: str = Field(min_length=3, max_length=150, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ0-9\s\-\.&]+$")
    descripcionOferta: str = Field(min_length=10, max_length=1000, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ0-9\s,.!?¿¡:;()\-\"\'\+@#]+$")
    salarioOfrecido: Decimal = Field(ge=0)
    ciudadOferta: str = Field(default=None, min_length=3, max_length=100, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    paisOferta: PaisOferta
    fechaPublicacion: date
    modalidadOferta: ModalidadOferta
    tipoContrato: TipoContrato
    jornadaLaboral: JornadaLaboral
    nivelExperiencia: NivelExperiencia
    nivelEstudios: NivelEstudios
    correoContacto: EmailStr = Field(min_length=6, max_length=150)
    imagenUrl: HttpUrl | None = None

    @model_validator(mode="after")
    def validar_fecha_publicacion(self):
        if self.fechaPublicacion > date.today():
            raise ValueError('La fecha de publicación no puede ser futura')
        return self