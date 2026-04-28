from src.modelDto.usuario_dto import UsuarioLogin, UsuarioRegister
from src.service.login_service import loginService
from fastapi import APIRouter

login_router = APIRouter(tags=["Autenticacion"])

@login_router.post("/login")
async def login_endpoint(usuario: UsuarioLogin):
    return await loginService.Login(usuario)

@login_router.post("/register")
async def login_endpoint(usuario: UsuarioRegister):
    return await loginService.register(usuario)