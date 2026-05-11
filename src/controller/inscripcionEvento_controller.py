from fastapi import APIRouter
from src.service.inscripcionEvento_crud import InscripcionEventoService
from src.modelDto.inscripcionEvento_dto import InscripcionEventoDto, ActualizarAsistenciaDto

inscripcion_router = APIRouter(prefix="/inscripciones", tags=["Inscripción Eventos"])

@inscripcion_router.post("/inscribir")
async def inscribir_egresado(inscripcion: InscripcionEventoDto):
    return await InscripcionEventoService.inscribir_egresado(
        inscripcion.idEgresado,
        inscripcion.idEvento
    )

@inscripcion_router.get("/evento/{idEvento}")
async def obtener_inscripciones_por_evento(idEvento: int):
    return await InscripcionEventoService.obtener_inscripciones_por_evento(idEvento)

@inscripcion_router.get("/egresado/{idEgresado}")
async def obtener_inscripciones_por_egresado(idEgresado: int):
    return await InscripcionEventoService.obtener_inscripciones_por_egresado(idEgresado)

@inscripcion_router.patch("/asistencia/{idInscripcion}")
async def actualizar_asistencia(idInscripcion: int, asistencia: ActualizarAsistenciaDto):
    return await InscripcionEventoService.actualizar_asistencia(
        idInscripcion,
        asistencia.estadoAsistencia
    )