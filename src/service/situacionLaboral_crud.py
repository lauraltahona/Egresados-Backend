from src.config.supabase_client import supabase

class SituacionLaboral_Service:
    def __init__(self):
        pass

    def crear_situacion_laboral(situacion: dict):
        try:
            existeEgresado = supabase.table("Egresados")\
                .select("idEgresado, nombre, apellidos")\
                .eq("idEgresado", situacion.idEgresado).execute()
            
            if not existeEgresado.data: return {"error": "el egresado no existe"}

            situacionJSON = {
                "estaEmpleado": situacion.estaEmpleado,
                "empresaActual": situacion.empresaActual,
                "cargoActual": situacion.cargoActual,
                "sectorEmpresa": situacion.sectorEmpresa,
                "sectorEmpresaOtro": situacion.sectorEmpresaOtro,
                "tipoContrato": situacion.tipoContrato,
                "salarioActual": situacion.salarioActual,
                "fechaIngreso": situacion.fechaIngreso,
                "idEgresado": situacion.idEgresado
            }
            
            response = supabase.table("Egresados")\
                .insert(situacionJSON).execute()
            
            return {"message": "Situación laboral creada exitosamente", "data": response.data}
            
        except Exception as e:
            return {"error": str(e)}

    def obtener_situacion_laboral_por_egresado(idEgresado: int):
        try:
            response = supabase.table("SituacionLaboral")\
                .select("*")\
                .eq("idEgresado", idEgresado).execute()
            if not response.data:
                return {"error": "No se encontró la situación laboral para el egresado especificado"}
            return {"data": response.data[0]}
        
        except Exception as e:
            return {"error": str(e)}
        
    def actualizar_situacion_laboral(idSituacion: int, situacion: dict):
        try:
            response = supabase.table("SituacionLaboral")\
                .update(situacion.dict())\
                .eq("idSituacion", idSituacion).execute()
            
            if response.status_code != 200:
                return {"error": "No se pudo actualizar la situación laboral"}
            
            return {"message": "Situación laboral actualizada exitosamente", "data": response.data}
        
        except Exception as e:
            return {"error": str(e)}

