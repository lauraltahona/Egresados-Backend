from pydantic import BaseModel, Field

class Proyecto(BaseModel):
    idProyecto: int # si es auto incremental quitar de todas las tablas
    tituloProyecto: str = Field(min_length=5, max_length=200, pattern=r"^[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]+$")
    rutaDocumento: str #validar el tipo de extension
    estadoProyecto: str # mmm para q quiero saber el estado en esta aplicacion? no me lo van a revisar
    descripcionProyecto: str = Field(min_length=10, max_length=500, pattern=r"^[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]+$")
    idEgresado: int