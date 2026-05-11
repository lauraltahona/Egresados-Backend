from datetime import date
from fastapi import HTTPException
from src.config.supabase_client import supabase
import src.enum.evento_enum as EventoEnum

class InscripcionEventoService:

    async def inscribir_egresado(idEgresado: int, idEvento: int):
        try:
            egresado = supabase.table("Egresados") \
                .select("idEgresado") \
                .eq("idEgresado", idEgresado).execute()
            if not egresado.data:
                raise HTTPException(status_code=404, detail="El egresado no existe")

            evento = supabase.table("Eventos") \
                .select("idEvento, estadoEvento") \
                .eq("idEvento", idEvento).execute()
            if not evento.data:
                raise HTTPException(status_code=404, detail="El evento no existe")

            estadoEvento = evento.data[0]["estadoEvento"]
            if estadoEvento == EventoEnum.EstadoEvento.CANCELADO:
                return {"error": "No se puede inscribir en un evento cancelado"}

            inscripcionExiste = supabase.table("InscripcionesEventos") \
                .select("idInscripcion") \
                .eq("idEgresado", idEgresado) \
                .eq("idEvento", idEvento).execute()
            if inscripcionExiste.data:
                return {"error": "El egresado ya está inscrito en este evento"}

            inscripcion = {
                "fechaInscripcion": date.today().isoformat(),
                "estadoAsistencia": False,
                "idEgresado": idEgresado,
                "idEvento": idEvento
            }

            response = supabase.table("InscripcionesEventos").insert(inscripcion).execute()
            return {"mensaje": "Inscripción realizada exitosamente", "data": response.data}

        except HTTPException as e:
            raise e
        except Exception as e:
            return {"error": str(e)}

    async def obtener_inscripciones_por_evento(idEvento: int):
        try:
            response = supabase.table("InscripcionesEventos") \
                .select("*, Egresados(nombreEgresado, apellidosEgresado, correoEgresado)") \
                .eq("idEvento", idEvento).execute()
            return {"data": response.data}
        except Exception as e:
            return {"error": str(e)}

    async def obtener_inscripciones_por_egresado(idEgresado: int):
        try:
            response = supabase.table("InscripcionesEventos") \
                .select("*, Eventos(nombreEvento, fechaEvento, modalidadEvento, estadoEvento)") \
                .eq("idEgresado", idEgresado).execute()
            return {"data": response.data}
        except Exception as e:
            return {"error": str(e)}

    async def actualizar_asistencia(idInscripcion: int, estadoAsistencia: bool):
        try:
            inscripcion = supabase.table("InscripcionesEventos") \
                .select("idInscripcion") \
                .eq("idInscripcion", idInscripcion).execute()
            if not inscripcion.data:
                raise HTTPException(status_code=404, detail="Inscripción no encontrada")

            response = supabase.table("InscripcionesEventos") \
                .update({"estadoAsistencia": estadoAsistencia}) \
                .eq("idInscripcion", idInscripcion).execute()

            return {"mensaje": "Asistencia actualizada correctamente", "data": response.data}
        except HTTPException as e:
            raise e
        except Exception as e:
            return {"error": str(e)}