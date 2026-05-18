from src.config.supabase_client import supabase

_cache = {}

def limpiar_cache():
    _cache.clear()


# ── Egresados ────────────────────────────────────────────────────────────────

def obtener_egresados_por_programa(id_programa: int):
    """
    Trae solo los ids y fecha de nacimiento de egresados de un programa
    La fecha de nacimiento se usa para calcular distribucion de edades en el service
    """
    clave = f"egresados_programa_{id_programa}"
    if clave in _cache:
        return _cache[clave]

    response = supabase.table("Egresados") \
        .select("idEgresado, fechaNacimiento") \
        .eq("idPrograma", id_programa) \
        .execute()

    _cache[clave] = response.data
    return response.data


def obtener_ids_egresados_por_programa(id_programa: int) -> list[int]:
    """
    Devuelve solo la lista de ids. Util para filtrar otras tablas.
    """
    egresados = obtener_egresados_por_programa(id_programa)
    return [e["idEgresado"] for e in egresados]


# ── Situacion Laboral ────────────────────────────────────────────────────────

def obtener_situacion_laboral_por_ids(ids_egresados: list[int]):
    """
    Trae situacion laboral de una lista de egresados.
    Solo los campos necesarios para los calculos de empleo.
    """
    if not ids_egresados:
        return []

    clave = f"situacion_laboral_{hash(tuple(sorted(ids_egresados)))}"
    if clave in _cache:
        return _cache[clave]

    response = supabase.table("situacionLaboral") \
        .select("idEgresado, estaEmpleado, salarioActual, sectorEmpresa, sectorEmpresaOtro") \
        .in_("idEgresado", ids_egresados) \
        .execute()

    _cache[clave] = response.data
    return response.data


# ── Ubicacion ────────────────────────────────────────────────────────────────

def obtener_ubicacion_por_ids(ids_egresados: list[int]):
    """
    Trae pais y ciudad de residencia de una lista de egresados.
    """
    if not ids_egresados:
        return []

    clave = f"ubicacion_{hash(tuple(sorted(ids_egresados)))}"
    if clave in _cache:
        return _cache[clave]

    response = supabase.table("Egresados") \
        .select("idEgresado, paisResidencia, ciudadResidencia") \
        .in_("idEgresado", ids_egresados) \
        .execute()

    _cache[clave] = response.data
    return response.data