from enum import Enum

class TipoEvento(str, Enum):
    CULTURAL = "Cultural"
    DEPORTIVO = "Deportivo"

class ModalidadEvento(str, Enum):
    PRESENCIAL = "Presencial"
    VIRTUAL = "Virtual"
    HIBRIDO = "Híbrido"

class EstadoEvento(str, Enum):
    PROGRAMADO = "Programado"
    EN_CURSO = "En curso"
    CANCELADO = "Cancelado"