from src.model.usuario import Usuario
from src.service.usuario_crud import UsuarioService
from fastapi import APIRouter

usuario_router = APIRouter(tags=["Usuario"])


@usuario_router.get("/usuarios")
async def leer_usuarios_endpoint():
    return UsuarioService.leer_usuarios()

