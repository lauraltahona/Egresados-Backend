from datetime import date
from typing import Optional
from pydantic import EmailStr, BaseModel, Field
import src.enum.egresado_enum as Enum

class Egresado(BaseModel):
    idEgresado: int
    nombre: str = Field(pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$", min_length=3, max_length=100) 
    apellidos: str = Field(pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$", min_length=3, max_length=100),
    tipoDocumento: Enum.TipoDocumento
    cedula: str = Field(min_length=8, max_length=10)
    fechaNacimiento: date
    correo: EmailStr
    celular: str = Field(max_length=10)
    sexo: Enum.Sexo
    grupoEtnico: Enum.GrupoEtnico
    discapacidad: bool
    carnet: bool
    dominioSegundaLengua: bool
    programaCursado: str
    paisResidencia: str
    
    sexoOtro: Optional[str] = None
    segundaLengua: Optional[Enum.SegundaLengua] = None
    segundaLenguaOtro: Optional[str] = None
    programaCursadoOtro: Optional[str] = None