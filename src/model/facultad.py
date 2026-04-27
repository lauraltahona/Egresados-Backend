from enum import Enum
from pydantic import Field, EmailStr

class Facultad(str, Enum):
    idFacultad: int
    nombreFacultad: str = Field(min_length=3, max_length=100, pattern=r"^[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]+$")
    correoFacultad: EmailStr # validar que sea unicesar.edu.co ! 