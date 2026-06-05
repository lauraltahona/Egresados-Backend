from src.modelDto.proyecto_dto import ProyectoDto
from src.config.supabase_client import supabase
from fastapi import HTTPException

class ProyectoService:

    def __init__(self):
        pass

    async def crear_proyecto(proyecto: ProyectoDto):
        try: 

            existeProyecto = supabase.table("Proyectos")\
                .select("idProyecto")\
                .eq("tituloProyecto", proyecto.tituloProyecto).execute()
            
            if existeProyecto.data: raise HTTPException(status_code=400, detail="Ya existe un proyecto con ese título")

            response = supabase.table("Proyectos").insert(proyecto.model_dump(mode='json')).execute() 

            return { "mensaje": "Proyecto registrado correctamente" }
        
        except HTTPException as http_exc:
            raise http_exc
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    async def obtener_proyectos():
        try: 
            response = supabase.table("Proyectos").select("*").execute()
            return response.data
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    async def obtener_proyecto_por_titulo(titulo: str):
        try: 
            response = supabase.table("Proyectos").select("*").eq("tituloProyecto", titulo).execute()
            if not response.data:
                raise HTTPException(status_code=404, detail="Proyecto no encontrado")
            return response.data[0]
        
        except HTTPException as http_e:
            raise http_e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    async def cambiar_estado_proyecto(idProyecto: int, nuevo_estado: str):
        try: 
            response = supabase.table("Proyectos").update({"estadoProyecto": nuevo_estado}).eq("idProyecto", idProyecto).execute()
            if response.count == 0:
                raise HTTPException(status_code=404, detail="Proyecto no encontrado")
            
            return {"mensaje": "Estado del proyecto actualizado correctamente", "data": response.data}
        
        except HTTPException as http_e:
            raise http_e
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))