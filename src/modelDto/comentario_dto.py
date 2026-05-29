from datetime import date

from pydantic import BaseModel, Field

class ComentarioPublicacionDto(BaseModel):
    idPublicacionComunidad: int = Field(gt=0)
    idUsuario: str 
    idComentarioPadre: int | None = Field(None, gt=0)
    contenidoComentario: str = Field(min_length=5, max_length=2000, pattern=r"^[0-9A-Za-zñÑáéíóúÁÉÍÓÚ%.,:;()+\-\s]+$")
    fechaComentario: date