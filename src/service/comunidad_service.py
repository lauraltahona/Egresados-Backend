from src.modelDto.comunidad_dto import ComunidadDto, ComunidadUpdateDto
from typing import Optional
from src.config.supabase_client import supabase
from fastapi import HTTPException

class ComunidadService:

    async def crear_comunidad(comunidad_dto: ComunidadDto):
        try:
            response = supabase.table("Comunidades")\
                .insert(comunidad_dto.model_dump(mode="json")).execute()
            
            return {"message": "Comunidad creada exitosamente", "data": response.data}
        
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al crear la comunidad: {str(e)}")
        
    async def get_comunidades(self,
        idComunidad: Optional[int] = None,
        nombreComunidad: Optional[str] = None,
        tipoComunidad: Optional[str] = None,
        ):
        try:
            query = supabase.table("Comunidades").select("*")

            if idComunidad is not None:
                query = query.eq("idComunidad", idComunidad)
            if nombreComunidad is not None:
                query = query.ilike("nombreComunidad", f"%{nombreComunidad}%")
            if tipoComunidad is not None:
                query = query.eq("tipoComunidad", tipoComunidad)

            comunidades = query.execute()
            return {"data": comunidades.data}

        
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al obtener las comunidades: {str(e)}")
        

    async def actualizar_comunidad(idComunidad: int, comunidad_dto: ComunidadUpdateDto):
        try:
            datos_actualizar = comunidad_dto.model_dump(mode="json", exclude_unset=True, exclude_none=True) # Excluye campos no proporcionados o con valor None

            response = supabase.table("Comunidades")\
                .update(datos_actualizar)\
                .eq("idComunidad", idComunidad).execute()
            return {"message": "Comunidad actualizada exitosamente", "data": response.data}
        
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al actualizar la comunidad: {str(e)}")