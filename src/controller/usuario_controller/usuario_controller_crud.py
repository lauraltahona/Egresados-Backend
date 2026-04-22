from src.model.usuario import Usuario
from src.service.usuario_service.usuario_crud        import crear_usuario
from fastapi import APIRouter

usuario_router = APIRouter()

@usuario_router.post("/crear-usuario")
def crear_usuario_endpoint(usuario: Usuario):# valida que el json que entre sea de tipo usuario antes de "entrar" :p

    return crear_usuario(usuario.model_dump()) #se convierte a diccionario

