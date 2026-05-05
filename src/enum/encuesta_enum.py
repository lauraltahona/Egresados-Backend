from enum import Enum

class EstadoEncuesta(str, Enum):
    ACTIVA = "Activa"
    CERRADA = "Cerrada"
    BORRADOR = "Borrador"


class TipoEncuesta(str, Enum):
    ESTANDAR = "Estándar"
    PERSONALIZADA = "Personalizada"
    MIXTA = "Mixta"