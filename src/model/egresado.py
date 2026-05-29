from datetime import date
from typing import Optional
from pydantic import EmailStr, BaseModel, Field
import src.enum.egresado_enum as Enum

class Egresado(BaseModel):
    idEgresado: int
    nombre: str = Field(pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$", min_length=3, max_length=100) 
    apellidos: str = Field(pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$", min_length=3, max_length=100),
    tipoDocumento: Enum.TipoDocumento
    numeroDocumento: str = Field(min_length=8, max_length=10)
    fechaNacimiento: date
    correoEgresado: EmailStr | None = None
    esGraduado: bool
    fechaGrado: date | None = None
    celular: str = Field(max_length=10)
    sexo: Enum.Sexo
    grupoEtnico: Enum.GrupoEtnico
    discapacidad: bool
    carnet: bool
    dominioSegundaLengua: bool
    programaCursado: str
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
    segundaLengua: Optional[Enum.SegundaLengua] = None
    segundaLenguaOtro: Optional[str] = None
    programaCursadoOtro: Optional[str] = None