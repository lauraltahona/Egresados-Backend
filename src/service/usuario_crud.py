from src.config.supabase_client import supabase
from src.service.rol_crud import RolService

class UsuarioService:
    def __init__(self):
        pass

    def leer_usuarios():
        try:
            response = supabase.table("Usuarios")\
            .select(
                "idUsuario", 
                "nombreUsuario", 
                "apellidoUsuario", 
                "correo",
                "celular", 
                "idRol", 
                "fechaRegistroUsuario",
                "Roles!inner(nombreRol)"
            )\
            .not_.eq("Roles.nombreRol", "Egresado")\
            .execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}