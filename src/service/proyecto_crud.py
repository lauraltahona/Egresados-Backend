from src.config.supabase_client import supabase

class ProyectoService:

    def __init__(self):
        pass

    async def crear_proyecto(proyecto: dict):
        try: 

            existeProyecto = supabase.table("Proyectos")\
                .select("idProyecto")\
                .eq(proyecto.tituloProyecto)
            
            if existeProyecto.data: return {"error": "El titulo ya está registrado"}

            response = supabase.table("Proyectos").insert(proyecto).execute() # convertir a JSON

            return { "mensaje": "Proyecto registrado correctamente" }
        
        except Exception as e:
            return {"error": str(e)}
        
    async def obtener_proyectos():
        try: 
            response = supabase.table("Proyectos").select("*").execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}