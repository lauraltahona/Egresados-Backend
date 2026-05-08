from typing import Optional
from datetime import date
from pydantic import BaseModel, EmailStr, Field
import src.enum.egresado_enum as Enum

class EgresadoDto(BaseModel):
    nombreEgresado: str = Field(pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$", min_length=3, max_length=100) 
    apellidosEgresado: str = Field(pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$", min_length=3, max_length=100),
    tipoDocumento: Enum.TipoDocumento 
    numeroDocumento: str = Field(min_length=6, max_length=16)
    fechaNacimiento: date
    correoEgresado: EmailStr
    telefono: str = Field(max_length=10)
    sexo: Enum.Sexo
    grupoEtnico: Enum.GrupoEtnico
    discapacidad: bool
    carnet: bool
    dominioSegundaLengua: bool
    segundaLengua: Optional[Enum.SegundaLengua] = None
    idPrograma: int
    paisResidencia: str
    ciudadResidencia: str =  Field(pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$", min_length=2, max_length=100)
    departamentoResidencia: str = Field(pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$", min_length=2, max_length=100)
    direccion: str = Field(min_length=10, max_length=150)
    estratoSocioeconomico: int = Field(ge=1, le=6)
    nivelFormacionProfesional: Enum.NivelFormacion
    produccionIntelectual: bool
    nombreProduccionIntelectual: str = Field(pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$", min_length=2, max_length=150)
    experiencia: int = Field(ge=0, le=70)
    
    sexoOtro: Optional[str] = None
    segundaLenguaOtro: Optional[str] = None


class EgresadoUpdateDto(BaseModel):

    correoEgresado: Optional[EmailStr] = None
    telefono: Optional[str] = Field(default=None,max_length=10)
    sexo: Optional[Enum.Sexo] = None
    grupoEtnico: Optional[Enum.GrupoEtnico] = None
    discapacidad: Optional[bool] = None
    carnet: Optional[bool] = None
    dominioSegundaLengua: Optional[bool] = None
    segundaLengua: Optional[Enum.SegundaLengua] = None
    paisResidencia: Optional[str] = None
    ciudadResidencia: Optional[str] = Field(default=None, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$",
        min_length=2,
        max_length=100
    )
    departamentoResidencia: Optional[str] = Field(
        default=None,
        pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$",
        min_length=2,
        max_length=100
    )
    direccion: Optional[str] = Field(default=None,min_length=10,max_length=150)
    estratoSocioeconomico: Optional[int] = Field(default=None, ge=1, le=6)
    nivelFormacionProfesional: Optional[Enum.NivelFormacion] = None
    produccionIntelectual: Optional[bool] = None
    nombreProduccionIntelectual: Optional[str] = Field(
        default=None,
        pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$",
        min_length=2,
        max_length=150
    )
    experiencia: Optional[int] = Field(default=None,ge=0,le=70)
    sexoOtro: Optional[str] = None
    segundaLenguaOtro: Optional[str] = None