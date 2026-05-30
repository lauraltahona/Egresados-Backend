from typing import Optional
from datetime import date
from pydantic import BaseModel, EmailStr, Field
import src.enum.egresado_enum as Enum

class EgresadoDto(BaseModel):
    nombreEgresado: str = Field(pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$", min_length=3, max_length=100) 
    apellidosEgresado: str = Field(pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$", min_length=3, max_length=100)
    tipoDocumento: Enum.TipoDocumento | None = None
    numeroDocumento: str | None = Field(None, min_length=6, max_length=16) 
    fechaNacimiento: date | None = None
    correoEgresado: EmailStr | None = None
    telefono: str = Field(max_length=10) 
    sexo: Enum.Sexo | None = None
    grupoEtnico: Enum.GrupoEtnico | None = None
    discapacidad: bool | None = None
    carnet: bool | None = None
    dominioSegundaLengua: bool | None = None
    segundaLengua: Optional[Enum.SegundaLengua] | None = None
    idPrograma: int
    paisResidencia: Optional[str] | None = None
    ciudadResidencia: Optional[str] | None =  Field(None, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$", min_length=2, max_length=100)
    departamentoResidencia: Optional[str] | None = Field(None, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$", min_length=2, max_length=100)
    direccion: Optional[str] | None = Field(None, min_length=10, max_length=150)
    estratoSocioeconomico: Optional[int] | None= Field(default=None, ge=1, le=6)
    nivelFormacionProfesional: Enum.NivelFormacion | None = None
    produccionIntelectual: bool | None = None
    nombreProduccionIntelectual: Optional[str] | None = Field(None, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$", min_length=2, max_length=150)
    experiencia: int | None = Field(None, ge=0, le=70)
    
    sexoOtro: Optional[str] | None = None
    segundaLenguaOtro: Optional[str] | None= None
    esGraduado: Optional[bool] | None = None
    fechaGrado: Optional[date] | None = None



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
    
class EgresadoImportDto(BaseModel):
    nombre: str = Field(pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$", min_length=1, max_length=100)
    apellidos: str = Field(pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$", min_length=1, max_length=100)
    numeroDocumento: str = Field(min_length=8, max_length=10)
    programaCursado: str = Field(min_length=3, max_length=150)
    fechaGrado: date
