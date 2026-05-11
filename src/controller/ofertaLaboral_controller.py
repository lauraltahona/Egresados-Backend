from typing import Optional

from src.service.ofertaLaboral_service import OfertaLaboralService
from src.modelDto.ofertaLaboral_dto import OfertaLaboralDTO
from src.enum.ofertaLaboral_enum import ModalidadOferta, TipoContrato, JornadaLaboral, NivelExperiencia, NivelEstudios, PaisOferta
from fastapi import APIRouter

oferta_router = APIRouter(prefix="/ofertas-laborales", tags=["Ofertas Laborales"])

@oferta_router.post("/crear")
async def crear_oferta_laboral(oferta_laboral: OfertaLaboralDTO):
    return await OfertaLaboralService().crear_oferta_laboral(oferta_laboral)

@oferta_router.get("/listar")
async def listar_ofertas_laborales(
    modalidad: Optional[ModalidadOferta] = None,
    pais: Optional[PaisOferta] = None,
    tipoContrato: Optional[TipoContrato] = None,
    nivelEstudios: Optional[NivelEstudios] = None,
    salario: Optional[float] = None,
):
    return await OfertaLaboralService().obtener_ofertas_laborales(
        modalidad, pais, tipoContrato, nivelEstudios, salario)

@oferta_router.get("/buscar")
async def buscar_oferta_laboral_por_titulo(tituloOferta: str):
    return await OfertaLaboralService().obtener_oferta_laboral_por_titulo(tituloOferta)

