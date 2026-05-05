from enum import Enum

class EstadoAsistencia(str, Enum):
    ASISTIO = "Asistió"
    NO_ASISTIO = "No asistió"