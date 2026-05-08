import datetime

from fastapi import HTTPException

from src.modelDto.egresado_dto import EgresadoDto, EgresadoUpdateDto
from src.service.login_service import loginService
from src.config.supabase_client import supabase

class EgresadoService:


    async def crear_egresado(egresado: EgresadoDto):
        try:
            existeEgresado = supabase.table("Egresados")\
                .select("idEgresado")\
                .eq("numeroDocumento", egresado.numeroDocumento).execute()
            
            if existeEgresado.data:
                raise HTTPException(status_code=404, detail="El egresado ya existe")

            response = supabase.table('Egresados').insert(egresado.model_dump(mode='json')).execute()

            usuarioRegister = {
                "nombreUsuario": egresado.nombreEgresado,
                "apellidoUsuario": egresado.apellidosEgresado,
                "idRol": 2,
                "correo": egresado.correoEgresado,
                "contrasena": egresado.numeroDocumento,
                "celular": egresado.telefono,
                "fechaRegistoUsuario": datetime.datetime.now().isoformat()
            }

            response_usuario = await loginService.register(usuarioRegister)
            print(response_usuario)

            return {"message": "Egresado creado exitosamente", "data": response.data}
        
        except Exception as e:
            return {"message": "Error al crear el egresado", "error": str(e)}
            

    async def get_egresados():
        try:
            response = supabase.table('Egresados').select('*').execute()
            return response.data
        except Exception as e:
            return {"message": "Error al obtener los egresados", "error": str(e)}
    
    async def get_egresado_by_id(idEgresado: int):
        try:
            response = supabase.table('Egresados').select('*').eq('idEgresado', idEgresado).execute()
            if not response.data:
                raise HTTPException(status_code=404, detail="Egresado no encontrado")
            return response.data[0]
        except Exception as e:
            return {"message": "Error al obtener el egresado", "error": str(e)}


    async def eliminar_egresado(idEgresado: int):
        try:
            response = supabase.table('Egresados').delete().eq('idEgresado', idEgresado).execute()
            if response.count == 0:
                raise HTTPException(status_code=404, detail="Egresado no encontrado")
            
            return {"message": "Egresado eliminado exitosamente"}
        except Exception as e:
            return {"message": "Error al eliminar el egresado", "error": str(e)}


    async def actualizar_egresado(idEgresado: int, egresado: EgresadoUpdateDto):
        try: 
            datos_actualizar = egresado.model_dump(exclude_unset=True, exclude_none=True)

            response = supabase.table("Egresados")\
                .update(datos_actualizar)\
                .eq("idEgresado", idEgresado).execute()

            return {"message": "Egresado actualizado correctamente",
                    "data": response.data}

        except Exception as e:
            raise HTTPException(status_code = 500, detail=f"Error al actualizar el egresado: {str(e)}")    