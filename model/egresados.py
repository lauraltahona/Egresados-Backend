from enum import Enum
from datetime import date
from typing import Optional

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

class Egresado:
    nombre: str
    apellidos: str
    cedula: str
    fechaNacimiento: date
    correo: str
    celular: str
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