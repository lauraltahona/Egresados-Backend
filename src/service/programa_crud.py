from src.config.supabase_client import supabase
class ProgramaService:
    
    def __init__(self):
        pass
    
    def crear_programa(programa: dict):
        try:
            response = supabase.table("Programas").insert(programa).execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}
        
    def leer_programas():
        try:
            response = supabase.table("Programas").select("*").execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}
        
    def leer_programas_por_facultad(id_facultad: int):
        try:
            response = supabase.table("Programas").select("*").eq("idFacultad", id_facultad).execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}
        
    def actualizar_programa(id_programa: int, programa: dict):
        try:
            response = supabase.table("Programas").update(programa).eq("idPrograma", id_programa).execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}
        
    def eliminar_programa(id_programa: int):
        try:
            response = supabase.table("Programas").delete().eq("idPrograma", id_programa).execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}