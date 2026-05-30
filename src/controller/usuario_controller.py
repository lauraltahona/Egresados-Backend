from src.model.usuario import Usuario
from src.service.usuario_crud import UsuarioService
from fastapi import APIRouter
from typing import Optional

usuario_router = APIRouter(tags=["Usuario"])

@usuario_router.get("/usuarios")
async def leer_usuarios_endpoint(
    idUsuario: Optional[int] = None,
    nombreUsuario: Optional[str] = None,
    correo: Optional[str] = None
):
    print(f"Recibido idUsuario: {idUsuario}, nombreUsuario: {nombreUsuario}, correo: {correo}")
    return await UsuarioService.leer_usuarios(idUsuario, nombreUsuario, correo)
