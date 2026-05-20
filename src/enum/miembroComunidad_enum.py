from enum import Enum

class RolMiembro(str, Enum):
    ADMINISTRADOR = "Administrador"
    MIEMBRO = "Miembro"
    MODERADOR = "Moderador"

class EstadoMiembro(str, Enum):
    ACTIVO = "Activo"
    INACTIVO = "Inactivo"
    BLOQUEADO = "Bloqueado"
    