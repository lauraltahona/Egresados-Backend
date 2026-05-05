from fastapi import APIRouter
from src.service.programa_crud import ProgramaService
from src.modelDto.programa_dto import ProgramaDto


programa_router = APIRouter(prefix="/programa", tags=["Programa"])

@programa_router.post("/crear")
def crear_programa_endpoint(programa: ProgramaDto):
    return ProgramaService.crear_programa(programa.model_dump())


@programa_router.get("/leer")
def leer_programas_endpoint():
    return ProgramaService.leer_programas()

@programa_router.get("/facultad/{id_facultad}")
def leer_programas_por_facultad_endpoint(id_facultad: int):
    return ProgramaService.leer_programas_por_facultad(id_facultad)


@programa_router.put("/actualizar/{id_programa}")
def actualizar_programa_endpoint(id_programa: int, programa: ProgramaDto):
    datos_actualizar = {k: v for k, v in programa.model_dump().items() if v is not None}
    return ProgramaService.actualizar_programa(id_programa, datos_actualizar)


@programa_router.delete("/eliminar/{id_programa}")
def eliminar_programa_endpoint(id_programa: int):
    return ProgramaService.eliminar_programa(id_programa)