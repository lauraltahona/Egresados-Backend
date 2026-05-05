from pydantic import BaseModel, Field
import src.enum.programa_enum as Enum

class Programa(BaseModel):

    idPrograma: int
    nombrePrograma: str
    nivelPrograma: Enum.NivelPrograma
    estadoPrograma: Enum.EstadoPrograma
    idFacultad: int
    tituloOtorgado: str = Field(pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    
