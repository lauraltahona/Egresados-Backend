from src.model.usuario import Usuario
import src.service.usuario_service.usuario_crud as usuario_service
from fastapi import APIRouter

usuario_router = APIRouter()

@usuario_router.post("/crear-usuario")
def crear_usuario_endpoint(usuario: Usuario):# valida que el json que entre sea de tipo usuario antes de "entrar" :p

    return usuario_service.crear_usuario(usuario.model_dump()) #se convierte a diccionario

@usuario_router.get("/usuarios")
def leer_usuarios_endpoint():
    return usuario_service.leer_usuarios()

