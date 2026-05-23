from datetime import date

from src.modelDto.miembroComunidad_dto import MiembroComunidadDto
from src.service.miembroComunidad_service import MiembroComunidadService
from src.modelDto.comunidad_dto import ComunidadDto, ComunidadUpdateDto
from typing import Optional
from src.config.supabase_client import supabase
from fastapi import HTTPException

class ComunidadService:

    async def crear_comunidad(comunidad_dto: ComunidadDto, idEgresado: int):
        try:
            response = supabase.table("Comunidades")\
                .insert(comunidad_dto.model_dump(mode="json")).execute()
            
            idComunidad = response.data[0]["idComunidad"]  # Obtener el ID de la comunidad recién creada

            # Crear el miembro fundador en la tabla MiembrosComunidad
            miembro = MiembroComunidadDto(
                rolMiembro="Administrador",
                estadoMiembro=True,
                fechaIngreso=date.today().isoformat(),
                idComunidad=idComunidad,
                idEgresado=idEgresado,
            )

            response_miembro = await MiembroComunidadService.crear_miembro_comunidad(miembro)
            
            return {"message": "Comunidad creada exitosamente", "data": response.data}
        
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al crear la comunidad: {str(e)}")
    

    async def unirse_comunidad(idComunidad: int, idEgresado: int):
        try:
            # Verificar si la comunidad existe
            comunidad = supabase.table("Comunidades").select("*").eq("idComunidad", idComunidad).execute()
            if not comunidad.data:
                raise HTTPException(status_code=404, detail="Comunidad no encontrada")

            # Verificar si el egresado ya es miembro de la comunidad
            miembro_existente = supabase.table("MiembrosComunidades").select("*")\
                .eq("idComunidad", idComunidad).eq("idEgresado", idEgresado).execute()
            if miembro_existente.data:
                raise HTTPException(status_code=400, detail="El egresado ya es miembro de la comunidad")
            
            # Crear el nuevo miembro con rol "Miembro"
            nuevo_miembro = MiembroComunidadDto(
                rolMiembro="Miembro",
                estadoMiembro=True,
                fechaIngreso=date.today().isoformat(),
                idComunidad=idComunidad,
                idEgresado=idEgresado,
            )

            response_miembro = await MiembroComunidadService.crear_miembro_comunidad(nuevo_miembro)
            return response_miembro
        
        except HTTPException:
            raise 
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al unirse a la comunidad: {str(e)}")


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
        

    async def eliminar_comunidad(idComunidad: int):
        try:
            response = supabase.table("Comunidades")\
                .delete().eq("idComunidad", idComunidad).execute()
            
            if response.count == 0:
                raise HTTPException(status_code=404, detail="Comunidad no encontrada")
            
            return {"message": "Comunidad eliminada exitosamente"}
        
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al eliminar la comunidad: {str(e)}")