from typing import Optional

from src.config.supabase_client import supabase
from src.service.rol_crud import RolService

class UsuarioService:
    def __init__(self):
        pass

    def leer_usuarios(idUsuario: Optional[str] = None, nombreUsuario: Optional[str] = None, correo: Optional[str] = None):
        try:
            query = supabase.table("Usuarios")\
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
            
            if idUsuario is not None:
                response = query.eq("idUsuario", idUsuario)
            if nombreUsuario is not None:
                response = query.ilike("nombreUsuario", f"%{nombreUsuario}%")
            if correo is not None:
                response = query.ilike("correo", f"%{correo}%")
            
            response = query.execute()

            return response.data
        except Exception as e:
            return {"error": str(e)}