from enum import Enum

class CategoriaReconocimiento(str, Enum):
    PROFESIONAL = "Profesional"
    INVESTIGACION = "Investigación"
    EMPRESARIAL = "Empresarial"
    SOCIAL_COMUNITARIO = "Social/Comunitario"
    CULTURAL = "Cultural"
    DEPORTIVO = "Deportivo"