from src.config.supabase_client import supabase

def crear_usuario(usuario: dict):
    try:
        response = supabase.table("Usuarios").insert(usuario).execute()
        return response.data
    except Exception as e:
        return {"error": str(e)}