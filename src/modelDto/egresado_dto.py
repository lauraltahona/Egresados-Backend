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