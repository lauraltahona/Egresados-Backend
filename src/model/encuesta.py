from enum import Enum
from datetime import date
from pydantic import BaseModel, Field


class EstadoEncuesta(str, Enum):
    ACTIVA = "Activa"
    CERRADA = "Cerrada"
    BORRADOR = "Borrador"


class TipoEncuesta(str, Enum):
    ESTANDAR = "Estándar"
    PERSONALIZADA = "Personalizada"
    MIXTA = "Mixta"


class Encuesta(BaseModel):
    idEncuesta: int
    tituloEncuesta: str = Field(min_length=5, max_length=200, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ0-9\s]+$")
    descripcionEncuesta: str = Field(min_length=10, max_length=500, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ0-9\s,.!?¿¡:;()\-]+$")
    fechaInicioEncuesta: date
    fechaVencimientoEncuesta: date
    estadoEncuesta: EstadoEncuesta
    tipoEncuesta: TipoEncuesta
    
    @classmethod
    def validar_fechas(cls, values):
        if "fechaInicioEncuesta" in values and "fechaVencimientoEncuesta" in values:
            inicio = values["fechaInicioEncuesta"]
            vencimiento = values["fechaVencimientoEncuesta"]
            if inicio >= vencimiento:
                raise ValueError(
                    "La fecha de inicio de la encuesta debe ser anterior a la fecha de vencimiento"
                )
        return values