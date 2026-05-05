from enum import Enum

class Sexo(str, Enum):
    MASCULINO = "Masculino"
    FEMENINO = "Femenino"
    PREFIERO_NO_DECIRLO = "Prefiero no decirlo"
    OTRO = "Otro"


class GrupoEtnico(str, Enum):
    NEGRO = "Negro, mulato o afrocolombiano"
    INDIGENAS = "Pueblos indígenas"
    RAIZALES = "Raizales del archipiélago de San Andrés, Providencia y Santa Catalina"
    PALENQUEROS = "Palenqueros"
    ROM = "RROM o Gitanos"
    NINGUNO = "Ninguno"


class SegundaLengua(str, Enum):
    INGLES = "Ingles"
    FRANCES = "Frances"
    PORTUGUES = "Portugués"
    ALEMAN = "Aleman"
    CHINO_MANDARIN = "Chino Mandarin"
    OTRO = "Otro"

class TipoDocumento(str, Enum):
    CEDULA_CIUDADANIA = "Cédula de ciudadanía"
    TARJETA_IDENTIDAD = "Tarjeta de identidad"
    PASAPORTE = "Pasaporte"
    CEDULA_EXTRANJERIA = "Cédula de extranjería"

class NivelFormacion(str, Enum):
    PREGRADO = "Pregrado"
    POSGRADO = "Posgrado"
    ESPECIALIZACION = "Especialización"
    MAESTRIA = "Maestría"
    DOCTORADO = "Doctorado"
    POSDOCTORADO = "Pos-Doctorado"