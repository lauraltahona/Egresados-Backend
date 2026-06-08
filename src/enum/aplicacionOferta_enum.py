from enum import Enum

class EstadoAplicacion(str, Enum):
    ENVIADA = "Enviada"
    EN_REVISION = "En revisión"
    SELECCIONADO = "Seleccionado"
    DESCARTADO = "Descartado"
    CONTRATADO = "Contratado"