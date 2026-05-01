from enum import Enum
from datetime import date
from typing import Optional
from pydantic import EmailStr, BaseModel, Field

class Sexo(str, Enum):
    MASCULINO = "Masculino"
    FEMENINO = "Femenino"
    PREFIERO_NO_DECIRLO = "Prefiero no decirlo"
    OTRO = "Otro"


class GrupoEtnico(str, Enum):
    NEGRO = "Negro, mulato o afrocolombiano"
    INDIGENAS = "Pueblos indígenas"
    RAIZALES = "Raizales del archipiélago de San Andrés, Providencia y Santa Catalina"
    PALENQUEROS = "Palenqueros"
    ROM = "RROM o Gitanos"
    NINGUNO = "Ninguno"


class SegundaLengua(str, Enum):
    INGLES = "Ingles"
    FRANCES = "Frances"
    PORTUGUES = "Portugués"
    ALEMAN = "Aleman"
    CHINO_MANDARIN = "Chino Mandarin"
    OTRO = "Otro"

class TipoDocumento(str, Enum):
    CEDULA_CIUDADANIA = "Cédula de ciudadanía"
    TARJETA_IDENTIDAD = "Tarjeta de identidad"
    PASAPORTE = "Pasaporte"
    CEDULA_EXTRANJERIA = "Cédula de extranjería"

class NivelFormacion(str, Enum):
    PREGRADO = "Pregrado"
    POSGRADO = "Posgrado"
    ESPECIALIZACION = "Especialización"
    MAESTRIA = "Maestría"
    DOCTORADO = "Doctorado"
    POSDOCTORADO = "Pos-Doctorado"


class Egresado(BaseModel):
    idEgresado: int
    nombre: str = Field(pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$", min_length=3, max_length=100) 
    apellidos: str = Field(pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$", min_length=3, max_length=100),
    tipoDocumento: TipoDocumento
    cedula: str = Field(min_length=8, max_length=10)
    fechaNacimiento: date
    correo: EmailStr
    celular: str = Field(max_length=10)
    sexo: Sexo
    grupoEtnico: GrupoEtnico
    discapacidad: bool
    carnet: bool
    dominioSegundaLengua: bool
    programaCursado: str
    paisResidencia: str
    
    sexoOtro: Optional[str] = None
    segundaLengua: Optional[SegundaLengua] = None
    segundaLenguaOtro: Optional[str] = None
    programaCursadoOtro: Optional[str] = None