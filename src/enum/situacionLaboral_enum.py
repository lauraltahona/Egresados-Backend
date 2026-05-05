from enum import Enum

class SectorEmpresa(str, Enum):
    TECNOLOGIA = "Tecnología"
    SALUD = "Salud"
    EDUCACION = "Educación"
    COMERCIO = "Comercio"
    INDUSTRIA = "Industria"
    GOBIERNO = "Gobierno"
    OTRO = "Otro"

class TipoContrato(str, Enum):
    TERMINO_FIJO = "Término fijo"
    TERMINO_INDEFINIDO = "Término indefinido"
    PRESTACION_SERVICIOS = "Prestación de servicios"
    POR_OBRA = "Por obra"