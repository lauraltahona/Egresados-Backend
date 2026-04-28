from src.config.supabase_client import supabase

class RolService:
    def __init__(self):
        pass
        
    def crear_rol(rol: dict):
        try:
            response = supabase.table("Roles").insert(rol).execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}
        
    def leer_roles():
        try:
            response = supabase.table("Roles").select("*").execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}

    def actualizar_rol(id_rol: int, rol: dict):
        try:
            response = supabase.table("Roles").update(rol).eq("idRol", id_rol).execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}
    
    def eliminar_rol(id_rol: int):
        try:
            response = supabase.table("Roles").delete().eq("idRol", id_rol).execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}