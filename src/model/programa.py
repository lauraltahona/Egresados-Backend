from pydantic import BaseModel, Field
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


class Programa(BaseModel):

    idPrograma: int
    nombrePrograma: str
    programaCursadoOtro: str
    nivelPrograma: NivelPrograma
    estadoPrograma: EstadoPrograma
    idFacultad: int
    tituloOtorgado: str = Field(pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    
