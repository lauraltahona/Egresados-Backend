from fastapi import APIRouter, UploadFile, File
from src.service.excel_service.excel_egresado_service import ExcelEgresadoService

excel_router = APIRouter(prefix="/excel", tags=["Excel"])


@excel_router.get("/egresados/exportar")
async def exportar_egresados():
    return await ExcelEgresadoService.exportar_egresados()


@excel_router.post("/egresados/importar")
async def importar_egresados(archivo: UploadFile = File(...)):
    return await ExcelEgresadoService.importar_egresados(archivo)


@excel_router.get("/egresados/plantilla")
async def descargar_plantilla():
    return await ExcelEgresadoService.descargar_plantilla()