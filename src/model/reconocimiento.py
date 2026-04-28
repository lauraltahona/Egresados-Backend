from enum import Enum
from datetime import date
from typing import Optional
from pydantic import BaseModel, Field, validator


class CategoriaReconocimiento(str, Enum):
    PROFESIONAL = "Profesional"
    INVESTIGACION = "Investigación"
    EMPRESARIAL = "Empresarial"
    SOCIAL_COMUNITARIO = "Social/Comunitario"
    CULTURAL = "Cultural"
    DEPORTIVO = "Deportivo"


class Reconocimiento(BaseModel):
    idReconocimiento: int
    nombreReconocimiento: str = Field(min_length=5, max_length=100, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ\s]+$")
    categoriaReconocimiento: CategoriaReconocimiento
    descripcionLogro: str = Field(min_length=20, max_length=1000, pattern=r"^[A-Za-zñÑáéíóúÁÉÍÓÚ0-9\s,.!?¿¡:;()\-\"\'@#]+$")