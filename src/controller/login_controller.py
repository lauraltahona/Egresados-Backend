from typing import Optional

from src.service.usuario_crud import UsuarioService
from src.modelDto.usuario_dto import UsuarioLogin, UsuarioRegister, CambiarContrasenaDto
from src.service.login_service import loginService
from fastapi import APIRouter

login_router = APIRouter(tags=["Autenticacion y Usuario"])

@login_router.post("/login")
async def login_endpoint(usuario: UsuarioLogin):
    return await loginService.Login(usuario)

@login_router.post("/register")
async def login_endpoint(usuario: UsuarioRegister):
    return await loginService.register(usuario)


@login_router.get("/usuarios")
async def leer_usuarios_endpoint(
    idUsuario: Optional[str] = None,
    nombreUsuario: Optional[str] = None,
    correo: Optional[str] = None
):
    return await UsuarioService.leer_usuarios(idUsuario, nombreUsuario, correo)


@login_router.patch("/cambiar-contrasena")
async def cambiar_contrasena_endpoint(usuario: CambiarContrasenaDto):
    if not usuario.contrasenas_coinciden():
        return {"error": "La nueva contraseña y la confirmación no coinciden"}
 
    return await loginService.cambiar_contrasena(
        usuario.usuarioId,
        usuario.contrasenaActual,
        usuario.nuevaContrasena
    )