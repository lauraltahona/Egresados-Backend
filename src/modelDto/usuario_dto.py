from datetime import date
from pydantic import BaseModel, EmailStr, Field, field_validator
import re

def validar_fortaleza_contrasena(contrasena: str) -> str:
    if len(contrasena) < 8:
        raise ValueError("La contraseña debe tener al menos 8 caracteres")
    if not re.search(r"[A-Z]", contrasena):
        raise ValueError("La contraseña debe tener al menos una mayúscula")
    if not re.search(r"[a-z]", contrasena):
        raise ValueError("La contraseña debe tener al menos una minúscula")
    if not re.search(r"\d", contrasena):
        raise ValueError("La contraseña debe tener al menos un número")
    if not re.search(r"[!@#$%^&*()_+\-=\[\]{}|;:,.<>?/\\*]", contrasena):
        raise ValueError("La contraseña debe tener al menos un símbolo especial")
    return contrasena

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
    fechaRegistroUsuario: date = Field(default_factory=date.today)

    @field_validator("contrasena")
    @classmethod
    def contrasena_segura(cls, v):
        return validar_fortaleza_contrasena(v)
    
class CambiarContrasenaDto(BaseModel):
    usuarioId: str = Field(min_length=1)
    contrasenaActual: str = Field(min_length=6)
    nuevaContrasena: str = Field(min_length=8)
    confirmarContrasena: str = Field(min_length=8)

    @field_validator("nuevaContrasena")
    @classmethod
    def nueva_contrasena_segura(cls, v):
        return validar_fortaleza_contrasena(v)
 
    def contrasenas_coinciden(self) -> bool:
        return self.nuevaContrasena == self.confirmarContrasena