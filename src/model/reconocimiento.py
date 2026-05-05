from pydantic import BaseModel, Field, validator
import src.enum.reconocimiento_enum as Enum

class Reconocimiento(BaseModel):
    idReconocimiento: int
    nombreReconocimiento: str = Field(min_length=5, max_length=100, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    categoriaReconocimiento: Enum.CategoriaReconocimiento
    descripcionLogro: str = Field(min_length=20, max_length=1000, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ0-9\s,.!?¿¡:;()\-\"\'@#]+$")