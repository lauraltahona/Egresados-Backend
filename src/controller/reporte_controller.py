from fastapi import APIRouter
from src.service.reporte_service import ReporteService
from src.repository.reporte_repository import limpiar_cache

reporte_router = APIRouter(prefix="/reportes", tags=["Reportes"])


@reporte_router.get("/empleo/{id_programa}")
async def reporte_empleo(id_programa: int):
    return await ReporteService.reporte_empleo(id_programa)


@reporte_router.get("/ubicacion/{id_programa}")
async def reporte_ubicacion(id_programa: int):
    return await ReporteService.reporte_ubicacion(id_programa)


@reporte_router.get("/edades/{id_programa}")
async def reporte_edades(id_programa: int):
    return await ReporteService.reporte_edades(id_programa)


@reporte_router.get("/salarios-top/{id_programa}")
async def reporte_salarios_top(id_programa: int, top: int = 5):
    return await ReporteService.reporte_salarios_top(id_programa, top)


@reporte_router.delete("/cache")
def limpiar_cache_endpoint():
    """Limpia el cache en memoria. Llamar cuando se registren nuevos egresados."""
    limpiar_cache()
    return {"mensaje": "Cache limpiado correctamente"}