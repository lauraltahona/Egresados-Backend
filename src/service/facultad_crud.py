from src.config.supabase_client import supabase
import src.modelDto.facultad_dto as facultadDto

class FacultadService:
    def __init__(self):
        pass
    
    async def crear_facultad(facultad: dict):
        try:
            response = supabase.table("Facultades").insert(facultad).execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}
        
    async def leer_facultades():
        try:
            response = supabase.table("Facultades").select("*").execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}