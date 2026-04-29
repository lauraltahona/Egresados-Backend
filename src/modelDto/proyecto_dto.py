from pydantic import BaseModel, Field

class ProyectoDto(BaseModel):
    tituloProyecto: str = Field(min_length=5, max_length=200, pattern=r"^[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]+$")
    rutaDocumento: str 
    estadoProyecto: str
    descripcionProyecto: str = Field(min_length=10, max_length=500, pattern=r"^[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]+$")
    idEgresado: int