from datetime import date
from pydantic import BaseModel, EmailStr, Field

class UsuarioLogin(BaseModel):
    correo: EmailStr = Field(min_length=6, max_length=50)
    contrasena: str = Field(min_length=8)
    
class UsuarioRegister(BaseModel):
    nombreUsuario: str = Field(min_length=3, max_length=100, pattern=r"^[A-Za-záéíóúñÁÉÍÓÚÑ\s]+$")
    apellidoUsuario: str = Field(min_length=3, max_length=100, pattern=r"^[A-Za-záéíóúñÁÉÍÓÚÑ\s]+$")
    idRol: int
    correo: EmailStr = Field(min_length=6, max_length=50)
    contrasena: str = Field(min_length=8)
    celular: str = Field(min_length=10, max_length=10, pattern=r"^\d{10}$")
    fechaRegistoUsuario: date = Field(default_factory=date.today)