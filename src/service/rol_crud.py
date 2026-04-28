from src.config.supabase_client import supabase

class RolService:
    def __init__(self):
        pass
        
    async def crear_rol(rol: dict):
        try:
            response = await supabase.table("Roles").insert(rol).execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}
        
    async def leer_roles():
        try:
            response = await supabase.table("Roles").select("*").execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}