from datetime import date
from pydantic import BaseModel, EmailStr

class Usuario(BaseModel):
    nombreUsuario: str
    apellidoUsuario: str
    idRol: int
    correo: EmailStr
    celular: str