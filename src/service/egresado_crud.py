from datetime import date
from typing import Optional

from fastapi import HTTPException

from src.enum.egresado_enum import GrupoEtnico
from src.modelDto.egresado_dto import EgresadoDto, EgresadoUpdateDto
from src.modelDto.usuario_dto import UsuarioRegister
from src.service.login_service import loginService
from src.config.supabase_client import supabase
from src.repository.reporte_repository import limpiar_cache

class EgresadoService:


    async def crear_egresado(egresado: EgresadoDto):
        try:
            existeEgresado = supabase.table("Egresados")\
                .select("idEgresado")\
                .eq("numeroDocumento", egresado.numeroDocumento).execute()
            
            if existeEgresado.data:
                raise HTTPException(status_code=404, detail="El egresado ya existe")

            response = supabase.table('Egresados').insert(egresado.model_dump(mode='json')).execute()
            
            rolEgresado = supabase.table("Roles") \
                .select("idRol") \
                .eq("nombreRol", "Egresado") \
                .single() \
                .execute()
 
            if not rolEgresado.data:
                raise HTTPException(status_code=500, detail="No se encontró el rol 'Egresado' en la base de datos")

            usuarioRegister = UsuarioRegister(
                nombreUsuario=egresado.nombreEgresado,
                apellidoUsuario=egresado.apellidosEgresado,
                idRol=rolEgresado.data["idRol"],
                correo=egresado.correoEgresado,
                contrasena=egresado.numeroDocumento,
                celular=egresado.telefono,
                fechaRegistoUsuario=date.today().isoformat()
            )

            response_usuario = await loginService.register(usuarioRegister)

            limpiar_cache()
            return {"message": "Egresado creado exitosamente", "data": response.data}
        
        except HTTPException:
            raise

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al crear el egresado: {str(e)}")
            

    async def get_egresados(
    idPrograma: Optional[int] = None,
    sexo: Optional[str] = None,
    correoEgresado: Optional[str] = None,
    numeroDocumento: Optional[str] = None,
    paisResidencia: Optional[str] = None,
    ciudadResidencia: Optional[str] = None,
    grupoEtnico: Optional[GrupoEtnico] = None,
    discapacidad: Optional[bool] = None):
        try:
            query = supabase.table('Egresados').select("idEgresado, nombreEgresado, " \
            "apellidosEgresado, sexo, grupoEtnico, paisResidencia, ciudadResidencia, idPrograma")

            if idPrograma is not None:
                query = query.eq("idPrograma", idPrograma)
            if sexo is not None:
                query = query.eq("sexo", sexo)
            if correoEgresado is not None:
                query = query.eq("correoEgresado", correoEgresado)
            if numeroDocumento is not None:
                query = query.eq("numeroDocumento", numeroDocumento)
            if paisResidencia is not None:
                query = query.eq("paisResidencia", paisResidencia)
            if ciudadResidencia is not None:
                query = query.eq("ciudadResidencia", ciudadResidencia)
            if grupoEtnico is not None:
                query = query.eq("grupoEtnico", grupoEtnico.value)
            if discapacidad is not None:
                query = query.eq("discapacidad", discapacidad)

            response = query.execute()

            return {"data": response.data}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al obtener los egresados: {str(e)}")
    
    async def get_egresado_by_id(idEgresado: int):
        try:
            response = supabase.table('Egresados').select('*').eq('idEgresado', idEgresado).execute()
            if not response.data:
                raise HTTPException(status_code=404, detail="Egresado no encontrado")
            return response.data[0]
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al obtener el egresado: {str(e)}")


    async def eliminar_egresado(idEgresado: int):
        try:
            response = supabase.table('Egresados').delete().eq('idEgresado', idEgresado).execute()
            if response.count == 0:
                raise HTTPException(status_code=404, detail="Egresado no encontrado")
            
            return {"message": "Egresado eliminado exitosamente"}
        
        except HTTPException:
            raise
        
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error al eliminar el egresado: {str(e)}")


    async def actualizar_egresado(idEgresado: int, egresado: EgresadoUpdateDto):
        try: 
            datos_actualizar = egresado.model_dump(mode="json", exclude_unset=True, exclude_none=True)

            response = supabase.table("Egresados")\
                .update(datos_actualizar)\
                .eq("idEgresado", idEgresado).execute()
            
            limpiar_cache()

            return {"message": "Egresado actualizado correctamente",
                    "data": response.data}

        except Exception as e:
            raise HTTPException(status_code = 500, detail=f"Error al actualizar el egresado: {str(e)}")    