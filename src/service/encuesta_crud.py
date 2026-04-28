from src.config.supabase_client import supabase

class EncuestaService:
    def __init__(self):
        pass
    
    def crear_encuesta(encuesta: dict):
        try:
            response = supabase.table("Encuestas").insert(encuesta).execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}
    
    def leer_encuestas():
        try:
            response = supabase.table("Encuestas").select("*").execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}
    
    def leer_encuesta_por_id(id_encuesta: int):
        try:
            response = supabase.table("Encuestas").select("*").eq("idEncuesta", id_encuesta).execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}
    
    def actualizar_encuesta(id_encuesta: int, encuesta: dict):
        try:
            response = supabase.table("Encuestas").update(encuesta).eq("idEncuesta", id_encuesta).execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}
    
    def eliminar_encuesta(id_encuesta: int):
        try:
            response = supabase.table("Encuestas").delete().eq("idEncuesta", id_encuesta).execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}