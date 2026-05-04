from src.service.ofertaLaboral_service import OfertaLaboralService
from src.modelDto.ofertaLaboral_dto import OfertaLaboralDTO
from fastapi import APIRouter

oferta_router = APIRouter(prefix="/ofertas-laborales", tags=["Ofertas Laborales"])

@oferta_router.post("/crear")
async def crear_oferta_laboral(oferta_laboral: OfertaLaboralDTO):
    return await OfertaLaboralService().crear_oferta_laboral(oferta_laboral)

@oferta_router.get("/listar")
async def listar_ofertas_laborales():
    return await OfertaLaboralService().obtener_ofertas_laborales()

@oferta_router.get("/buscar")
async def buscar_oferta_laboral_por_titulo(tituloOferta: str):
    return await OfertaLaboralService().obtener_oferta_laboral_por_titulo(tituloOferta)

