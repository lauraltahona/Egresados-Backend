from datetime import date
from pydantic import BaseModel


class rol(BaseModel):
    nombreRol: str
    descripcionRol: str
    fechaActualizacionRol: date