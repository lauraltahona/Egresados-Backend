from enum import Enum

class TipoBeneficio(str, Enum):
    HOTELERIA = "Hotelería"
    TURISTICO = "Turístico"
    GASTRONOMICO = "Gastronómico"
    BOLSA_EMPLEO = "Bolsa de empleo"
    SALUD = "Salud"
    EDUCATIVO = "Educativo"
    OTRO = "Otro"

class EstadoConvenio(str, Enum):
    ACTIVO = "Activo"
    INACTIVO = "Inactivo"
    VENCIDO = "Vencido"
    EN_RENOVACION = "En renovación"