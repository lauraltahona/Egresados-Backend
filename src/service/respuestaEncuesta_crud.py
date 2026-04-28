from src.config.supabase_client import supabase

class RespuestaEncuestaService:
    def __init__(self):
        pass
    
    def crear_respuesta(respuesta: dict):
        try:
            response = supabase.table("RespuestasEncuestas").insert(respuesta).execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}
    
    def leer_respuestas():
        try:
            response = supabase.table("RespuestasEncuestas").select("*").execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}
    
    def leer_respuesta_por_id(id_respuesta: int):
        try:
            response = supabase.table("RespuestasEncuestas").select("*").eq("idRespuesta", id_respuesta).execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}
    
    def leer_respuestas_por_encuesta(id_encuesta: int):
        try:
            response = supabase.table("RespuestasEncuestas").select("*").eq("idEncuesta", id_encuesta).execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}
    
    def leer_respuestas_por_egresado(id_egresado: int):
        try:
            response = supabase.table("RespuestasEncuestas").select("*").eq("idEgresado", id_egresado).execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}
    
    def actualizar_respuesta(id_respuesta: int, respuesta: dict):
        try:
            response = supabase.table("RespuestasEncuestas").update(respuesta).eq("idRespuesta", id_respuesta).execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}
    
    def eliminar_respuesta(id_respuesta: int):
        try:
            response = supabase.table("RespuestasEncuestas").delete().eq("idRespuesta", id_respuesta).execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}