from pydantic import Field, EmailStr, BaseModel

class FacultadDto(BaseModel):
    nombreFacultad: str = Field(min_length=3, max_length=100, pattern=r"^[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]+$")
    correoFacultad: EmailStr