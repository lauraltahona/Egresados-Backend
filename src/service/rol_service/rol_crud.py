from src.config.supabase_client import supabase

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