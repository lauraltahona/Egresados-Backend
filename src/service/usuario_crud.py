from src.config.supabase_client import supabase
from src.service.rol_crud import RolService

class UsuarioService:
    def __init__(self):
        pass

    async def crear_usuario(usuario: dict):
        try:
            response = supabase.table("Usuarios").insert(usuario).execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}
        
    def leer_usuarios():
        try:
            response = supabase.table("Usuarios")\
            .select(
                "idUsuario", 
                "nombreUsuario", 
                "apellidoUsuario", 
                "celular", 
                "idRol", 
                "fechaRegistoUsuario",
                "Roles!inner(nombreRol)"
            )\
            .not_.eq("Roles.nombreRol", "Egresado")\
            .execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}