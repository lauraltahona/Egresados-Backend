from pydantic import BaseModel

class rolDto(BaseModel):
    nombreRol: str
    descripcionRol: str