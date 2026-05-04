from src.modelDto.ofertaLaboral_dto import OfertaLaboralDTO
from src.config.supabase_client import supabase
class OfertaLaboralService:

    async def crear_oferta_laboral(self, oferta_laboral: OfertaLaboralDTO):
        try:
            response = supabase.table("OfertasLaborales")\
                .insert(oferta_laboral.model_dump(mode='json')).execute()
            return {"message": "Oferta laboral creada exitosamente"}
        except Exception as e:
            return {"error": str(e)}
        
    async def obtener_ofertas_laborales(self):
        try:
            response = supabase.table("OfertasLaborales").select("*").execute()
            return {"data": response.data}
        except Exception as e:
            return {"error": str(e)}
        
    async def obtener_oferta_laboral_por_titulo(self, tituloOferta: str):
        try:
            response = supabase.table("OfertasLaborales")\
                .select("*").eq("tituloOferta", tituloOferta).execute()
            
            if not response.data:
                return {"error": "No se encontró la oferta laboral con el título especificado"}
            
            return {"data": response.data[0]}
        except Exception as e:
            return {"error": str(e)}
       