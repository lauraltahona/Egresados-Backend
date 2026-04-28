from datetime import date
from pydantic import BaseModel


class rol(BaseModel):
    idRol: int
    nombreRol: str
    descripcionRol: str
    fechaActualizacionRol: date