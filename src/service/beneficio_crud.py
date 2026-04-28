from src.config.supabase_client import supabase

class BeneficioService:
    def __init__(self):
        pass
    
    def crear_beneficio(beneficio: dict):
        try:
            response = supabase.table("Beneficios").insert(beneficio).execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}
    
    def leer_beneficios():
        try:
            response = supabase.table("Beneficios").select("*").execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}
    
    
    def actualizar_beneficio(id_beneficio: int, beneficio: dict):
        try:
            response = supabase.table("Beneficios").update(beneficio).eq("idBeneficio", id_beneficio).execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}
    
    def eliminar_beneficio(id_beneficio: int):
        try:
            response = supabase.table("Beneficios").delete().eq("idBeneficio", id_beneficio).execute()
            return response.data
        except Exception as e:
            return {"error": str(e)}