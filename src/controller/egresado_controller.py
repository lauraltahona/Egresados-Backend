from typing import Optional

from src.enum.egresado_enum import GrupoEtnico
from src.service.egresado_crud import EgresadoService
from src.modelDto.egresado_dto import EgresadoDto, EgresadoUpdateDto
from fastapi import APIRouter

egresado_router = APIRouter(tags=["Egresados"])

@egresado_router.post("/egresados")
async def crear_egresado(egresado: EgresadoDto):
    response = await EgresadoService.crear_egresado(egresado)
    return response

@egresado_router.get("/egresados")  
async def get_egresados(
    idPrograma: Optional[int] = None,
    sexo: Optional[str] = None,
    correoEgresado: Optional[str] = None,
    numeroDocumento: Optional[str] = None,
    paisResidencia: Optional[str] = None,
    ciudadResidencia: Optional[str] = None,
    grupoEtnico: Optional[GrupoEtnico] = None,
    discapacidad: Optional[bool] = None
):
    response = await EgresadoService.get_egresados(idPrograma, sexo, correoEgresado, numeroDocumento,paisResidencia, ciudadResidencia, grupoEtnico, discapacidad)
    return response

@egresado_router.get("/egresados/{idEgresado}")
async def get_egresado_by_id(idEgresado: int):
    response = await EgresadoService.get_egresado_by_id(idEgresado)
    return response 

@egresado_router.delete("/egresados/{idEgresado}")
async def eliminar_egresado(idEgresado: int):
    response = await EgresadoService.eliminar_egresado(idEgresado)
    return response

@egresado_router.patch("/egresados/{idEgresado}")
async def actualizar_egresado(idEgresado: int, egresado: EgresadoUpdateDto):
    response = await EgresadoService.actualizar_egresado(idEgresado, egresado)
    return response