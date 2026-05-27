from src.config.supabase_client import supabase
from src.modelDto.beneficio_dto import BeneficioDto, BeneficioDtoUpdate
from fastapi import HTTPException

class BeneficioService:
    
    async def crear_beneficio(beneficio: BeneficioDto):
        try:
            existeBeneficio = supabase.table("Beneficios").select("idBeneficio").eq("nombreBeneficio", beneficio.nombreBeneficio).execute()

            if existeBeneficio.data:
                raise HTTPException(status_code=402, detail="El nombre del beneficio ya existe")

            response = supabase.table("Beneficios").insert(beneficio.model_dump(mode="json")).execute()
            print(response)
            return response.data
        
        except HTTPException:
            raise
        except Exception as e:
            print(e)
            raise HTTPException(status_code=500, detail="Error en el servidor al crear beneficio")
    
    async def leer_beneficios():
        try:
            response = supabase.table("Beneficios").select("*").execute()
            return response.data
        except Exception as e:
            raise HTTPException("Error con el servidor al consultar beneficios")
    
    
    async def actualizar_beneficio(id_beneficio: int, beneficio: BeneficioDtoUpdate):
        try:
            response = supabase.table("Beneficios").update(beneficio).eq("idBeneficio", id_beneficio).execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}
        

    async def leer_beneficio_por_id(id_beneficio: int):
        try:
            response = supabase.table("Beneficios").select("*").eq("idBeneficio", id_beneficio).execute()
            return response.data
        except Exception as e:
            raise HTTPException(status_code=404, detail="beneficio no encontrado o error con el servidor")
        

    async def eliminar_beneficio(id_beneficio: int):
        try:
            response = supabase.table("Beneficios").delete().eq("idBeneficio", id_beneficio).execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}