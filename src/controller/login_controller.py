from src.modelDto.usuario_dto import UsuarioLogin, UsuarioRegister, CambiarContrasenaDto
from src.service.login_service import loginService
from fastapi import APIRouter

login_router = APIRouter(tags=["Autenticacion"])

@login_router.post("/login")
async def login_endpoint(usuario: UsuarioLogin):
    return await loginService.Login(usuario)

@login_router.post("/register")
async def login_endpoint(usuario: UsuarioRegister):
    return await loginService.register(usuario)

@login_router.patch("/cambiar-contrasena")
async def cambiar_contrasena_endpoint(usuario: CambiarContrasenaDto):
    if not usuario.contrasenas_coinciden():
        return {"error": "La nueva contraseña y la confirmación no coinciden"}
 
    return await loginService.cambiar_contrasena(
        usuario.usuarioId,
        usuario.contrasenaActual,
        usuario.nuevaContrasena
    )