from src.model.usuario import Usuario
from src.service.usuario_crud import UsuarioService
from fastapi import APIRouter

usuario_router = APIRouter(tags=["Usuario"])

@usuario_router.post("/crear-usuario")
async def crear_usuario_endpoint(usuario: Usuario):
    return await UsuarioService.crear_usuario(usuario.model_dump()) #se convierte a diccionario

