from enum import Enum

class TipoComunidad(str, Enum):
    ACADEMICA = "Académica"
    PROFESIONAL = "Profesional"
    INVESTIGATIVA = "Investigativa"
    LABORAL = "Laboral"
    SOCIAL = "Social"
    GENERAL = "General"
