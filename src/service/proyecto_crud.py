from src.modelDto.proyecto_dto import ProyectoDto
from src.config.supabase_client import supabase

class ProyectoService:

    def __init__(self):
        pass

    async def crear_proyecto(proyecto: ProyectoDto):
        try: 

            existeProyecto = supabase.table("Proyectos")\
                .select("idProyecto")\
                .eq("tituloProyecto", proyecto.tituloProyecto).execute()
            
            if existeProyecto.data: return {"error": "El titulo ya está registrado"}

            response = supabase.table("Proyectos").insert(proyecto.model_dump(mode='json')).execute() 

            return { "mensaje": "Proyecto registrado correctamente" }
        
        except Exception as e:
            return {"error": str(e)}
        
    async def obtener_proyectos():
        try: 
            response = supabase.table("Proyectos").select("*").execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}
        
    async def obtener_proyecto_por_titulo(titulo: str):
        try: 
            response = supabase.table("Proyectos").select("*").eq("tituloProyecto", titulo).execute()
            if not response.data:
                return {"error": "Proyecto no encontrado"}
            return response.data[0]
        
        except Exception as e:
            return {"error": str(e)}