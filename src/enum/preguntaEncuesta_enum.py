from enum import Enum

class TipoPregunta(str, Enum):
    SELECCION_UNICA = "Selección única"
    TEXTO_LIBRE = "Texto libre"