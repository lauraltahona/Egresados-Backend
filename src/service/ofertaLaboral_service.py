from typing import Optional

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
        
        
    async def obtener_ofertas_laborales(self, 
    modalidad: Optional[str] = None,
    pais: Optional[str] = None,
    tipo_contrato: Optional[str] = None,
    nivel_estudios: Optional[str] = None,
    salario: Optional[float] = None):
        try:
            query = supabase.table("OfertasLaborales").select("*")

            if modalidad is not None:
                query = query.eq("modalidadOferta", modalidad.value)
            if pais is not None:
                query = query.eq("paisOferta", pais.value)
            if tipo_contrato is not None:
                query = query.eq("tipoContrato", tipo_contrato.value)
            if nivel_estudios is not None:
                query = query.eq("nivelEstudios", nivel_estudios.value)
            if salario is not None:
                query = query.gte("salarioOfrecido", salario)

            response = query.execute()
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
       