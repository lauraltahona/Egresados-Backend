from src.config.supabase_client import supabase

class PreguntaEncuestaService:
    def __init__(self):
        pass
    
    def crear_pregunta(pregunta: dict):
        try:
            response = supabase.table("PreguntasEncuestas").insert(pregunta).execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}
    
    def leer_preguntas():
        try:
            response = supabase.table("PreguntasEncuestas").select("*").execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}
    
    
    def leer_preguntas_por_encuesta(id_encuesta: int):
        try:
            response = supabase.table("PreguntasEncuestas").select("*").eq("idEncuesta", id_encuesta).execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}
    
    def actualizar_pregunta(id_pregunta: int, pregunta: dict):
        try:
            response = supabase.table("PreguntasEncuestas").update(pregunta).eq("idPregunta", id_pregunta).execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}
    
    def eliminar_pregunta(id_pregunta: int):
        try:
            response = supabase.table("PreguntasEncuestas").delete().eq("idPregunta", id_pregunta).execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}