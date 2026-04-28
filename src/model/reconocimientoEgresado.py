from datetime import date
from pydantic import BaseModel, Field, validator

class ReconocimientoEgresado(BaseModel):
    idReconocimientoEgresado: int
    idEgresado: int = Field(gt=0)
    idReconocimiento: int = Field(gt=0)
    fechaReconocimiento: date
    eventoReconocimiento: str = Field(min_length=3, max_length=150, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ0-9\s]+$")
    documentoSoporte: str = Field(min_length=5, max_length=300, pattern=r"^[A-Za-z0-9_/\-\.]+\.pdf$")
    
    @validator('documentoSoporte')
    def validar_documento_soporte(cls, v):
        if not v.lower().endswith('.pdf'):
            raise ValueError('El documento de soporte debe tener extensión .pdf')
        return v