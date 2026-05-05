from src.config.supabase_client import supabase
from src.model.evento import Evento
import src.enum.evento_enum as Enum

class EventoService:
    
    def __init__(self):
        pass
    
    async def crear_evento (evento: dict):
        try:
            evento_existe = supabase.table("Eventos")\
                .select("idEvento")\
                .eq("nombreEvento", evento.get("nombreEvento"))\
                .eq("fechaEvento", evento.get("fechaEvento"))\
                .execute()
            
            if evento_existe.data:
                return {"error": "Ya existe un evento con el mismo nombre esa fecha"}
            
            if "estadoEvento" not in evento:
                evento["estadoEvento"] = Enum.EstadoEvento.PROGRAMADO
            
            response = supabase.table("Eventos").insert(evento).execute()
            
            if not response.data:
                return {"error": "No se pudo crear el evento"}
            
            return response.data
        
        except Exception as e:
            return {"error": str(e)}
        
    def leer_eventos():
        try:
            response = supabase.table("Eventos").select("*").order("fechaEvento", desc=False).execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}
            
    def leer_eventos_por_estado(estado: str):
        try:
            response = supabase.table("Eventos").select("*").eq("estadoEvento", estado)\
                .order("fechaEvento", desc=False)\
                .execute()
            
            return response.data
            
        except Exception as e:
            return {"error": str(e)}