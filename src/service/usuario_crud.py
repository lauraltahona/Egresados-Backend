from src.config.supabase_client import supabase

class UsuarioService:
    def __init__(self):
        pass

    async def crear_usuario(usuario: dict):
        try:
            response = await supabase.table("Usuarios").insert(usuario).execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}