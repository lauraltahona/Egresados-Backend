from enum import Enum

class TipoPublicacion(str, Enum):
    ANUNCIO = "Anuncio"
    EVENTO = "Evento"
    NOTICIA = "Noticia"
    DISCUSION = "Discusión"
    RECURSO = "Recurso"