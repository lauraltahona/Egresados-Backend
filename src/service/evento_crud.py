from src.config.supabase_client import supabase
from fastapi import HTTPException
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
        
    def leer_evento_por_id(idEvento: int):
        try:
            response = supabase.table("Eventos") \
                .select("*") \
                .eq("idEvento", idEvento) \
                .execute()

            if not response.data:
                raise HTTPException(status_code=404, detail="Evento no encontrado")

            return response.data
        except HTTPException as e:
            raise e
        except Exception as e:
            return {"error": str(e)}
        
    def actualizar_evento(idEvento: int, evento: dict):
        try:
            evento = supabase.table("Eventos") \
                .select("idEvento, estadoEvento") \
                .eq("idEvento", idEvento) \
                .execute()

            if not evento.data:
                raise HTTPException(status_code=404, detail="Evento no encontrado")

            if evento.data[0]["estadoEvento"] == Enum.EstadoEvento.CANCELADO:
                return {"error": "No se puede editar un evento cancelado"}

            response = supabase.table("Eventos") \
                .update(evento) \
                .eq("idEvento", idEvento) \
                .execute()

            return {"mensaje": "Evento actualizado correctamente", "data": response.data}

        except HTTPException as e:
            raise e
        except Exception as e:
            return {"error": str(e)}

    def actualizar_estado_evento(idEvento: int, estado: str):
        try:
            evento = supabase.table("Eventos") \
                .select("idEvento, estadoEvento") \
                .eq("idEvento", idEvento) \
                .execute()

            if not evento.data:
                raise HTTPException(status_code=404, detail="Evento no encontrado")

            estadoActual = evento.data[0]["estadoEvento"]

            transiciones_validas = {
                Enum.EstadoEvento.PROGRAMADO: [Enum.EstadoEvento.EN_CURSO, Enum.EstadoEvento.CANCELADO],
                Enum.EstadoEvento.EN_CURSO:   [Enum.EstadoEvento.CANCELADO],
                Enum.EstadoEvento.CANCELADO:  []
            }

            if estado not in transiciones_validas.get(estadoActual, []):
                return {
                    "error": f"No se puede cambiar el estado de '{estadoActual}' a '{estado}'"
                }

            response = supabase.table("Eventos") \
                .update({"estadoEvento": estado}) \
                .eq("idEvento", idEvento) \
                .execute()

            return {"mensaje": f"Estado actualizado a '{estado}'", "data": response.data}

        except HTTPException as e:
            raise e
        except Exception as e:
            return {"error": str(e)}

    def eliminar_evento(idEvento: int):
        try:
            evento = supabase.table("Eventos") \
                .select("idEvento") \
                .eq("idEvento", idEvento) \
                .execute()

            if not evento.data:
                raise HTTPException(status_code=404, detail="Evento no encontrado")

            # Verificar que no tenga inscripciones activas
            inscripciones = supabase.table("InscripcionesEventos") \
                .select("idInscripcion") \
                .eq("idEvento", idEvento) \
                .execute()

            if inscripciones.data:
                return {
                    "error": "No se puede eliminar el evento porque tiene inscripciones registradas"
                }

            supabase.table("Eventos").delete().eq("idEvento", idEvento).execute()

            return {"mensaje": "Evento eliminado correctamente"}

        except HTTPException as e:
            raise e
        except Exception as e:
            return {"error": str(e)}