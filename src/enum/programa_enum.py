from enum import Enum

class NivelPrograma(str, Enum):
    PREGRADO = "Pregrado"
    ESPECIALIZACION = "Especialización"
    MAESTRIA = "Maestría"
    DOCTORADO = "Doctorado"
    POSDOCTORADO = "Pos-Doctorado"

class EstadoPrograma(str, Enum):
    ACTIVO = "Activo"
    INACTIVO = "Inactivo"