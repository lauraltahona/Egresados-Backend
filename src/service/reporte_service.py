from datetime import date
from collections import Counter
from src.repository.reporte_repository import (
    obtener_egresados_por_programa,
    obtener_ids_egresados_por_programa,
    obtener_situacion_laboral_por_ids,
    obtener_ubicacion_por_ids,
)


def _contar_y_porcentaje(parte: int, total: int) -> dict:
    """Calculo comun: cantidad + porcentaje redondeado."""
    return {
        "cantidad": parte,
        "porcentaje": round((parte / total) * 100, 2) if total else 0
    }


def _distribucion(lista: list, clave: str) -> list[dict]:
    """
    Recibe una lista de dicts y agrupa por la clave dada.
    Devuelve lista ordenada de mayor a menor con cantidad y porcentaje.
    Util para sectores, ciudades, paises, rangos de edad, etc.
    """
    total = len(lista)
    conteo = Counter(item.get(clave) or "Sin especificar" for item in lista)
    return [
        {
            clave: valor,
            "cantidad": cantidad,
            "porcentaje": round((cantidad / total) * 100, 2)
        }
        for valor, cantidad in conteo.most_common()
    ]


def _calcular_edad(fecha_nacimiento_str: str) -> int | None:
    try:
        nacimiento = date.fromisoformat(fecha_nacimiento_str)
        hoy = date.today()
        return hoy.year - nacimiento.year - (
            (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day)
        )
    except Exception:
        return None


def _rango_edad(edad: int) -> str:
    if edad < 25:
        return "menor de 25"
    elif edad <= 30:
        return "25-30"
    elif edad <= 35:
        return "31-35"
    elif edad <= 40:
        return "36-40"
    else:
        return "mayor de 40"


# ── Reportes públicos ────────────────────────────────────────────────────────

class ReporteService:

    async def reporte_empleo(id_programa: int):
        """
        Indicadores de empleo para los egresados de un programa:
        - Total egresados
        - Empleados vs desempleados
        - Salario promedio
        - Distribucion por sector
        """
        try:
            ids = obtener_ids_egresados_por_programa(id_programa)
            if not ids:
                return {"mensaje": "No hay egresados registrados para este programa"}

            situaciones = obtener_situacion_laboral_por_ids(ids)
            total = len(situaciones)

            empleados = [s for s in situaciones if s.get("estaEmpleado")]
            desempleados = [s for s in situaciones if not s.get("estaEmpleado")]

            salarios = [
                float(s["salarioActual"])
                for s in empleados
                if s.get("salarioActual")
            ]
            salario_promedio = round(sum(salarios) / len(salarios), 2) if salarios else 0

            # Para sector usamos sectorEmpresa, y si es "Otro" tomamos sectorEmpresaOtro
            sectores_lista = [
                {
                    "sectorEmpresa": (
                        s.get("sectorEmpresaOtro")
                        if s.get("sectorEmpresa") == "Otro"
                        else s.get("sectorEmpresa")
                    ) or "Sin especificar"
                }
                for s in empleados
            ]

            return {
                "idPrograma": id_programa,
                "totalConSituacionLaboral": total,
                "empleados": _contar_y_porcentaje(len(empleados), total),
                "desempleados": _contar_y_porcentaje(len(desempleados), total),
                "salarioPromedio": salario_promedio,
                "distribucionSectores": _distribucion(sectores_lista, "sectorEmpresa"),
            }

        except Exception as e:
            return {"error": str(e)}


    async def reporte_ubicacion(id_programa: int):
        """
        Distribucion geografica de los egresados de un programa.
        """
        try:
            ids = obtener_ids_egresados_por_programa(id_programa)
            if not ids:
                return {"mensaje": "No hay egresados registrados para este programa"}

            ubicaciones = obtener_ubicacion_por_ids(ids)

            return {
                "idPrograma": id_programa,
                "totalEgresados": len(ids),
                "distribucionPorPais": _distribucion(ubicaciones, "paisResidencia"),
                "distribucionPorCiudad": _distribucion(ubicaciones, "ciudadResidencia"),
            }

        except Exception as e:
            return {"error": str(e)}


    async def reporte_edades(id_programa: int):
        """
        Distribucion de edades de los egresados de un programa.
        """
        try:
            egresados = obtener_egresados_por_programa(id_programa)
            if not egresados:
                return {"mensaje": "No hay egresados registrados para este programa"}

            rangos = []
            for e in egresados:
                edad = _calcular_edad(e.get("fechaNacimiento", ""))
                if edad is not None:
                    rangos.append({"rangoEdad": _rango_edad(edad)})

            return {
                "idPrograma": id_programa,
                "totalEgresados": len(egresados),
                "distribucionEdades": _distribucion(rangos, "rangoEdad"),
            }

        except Exception as e:
            return {"error": str(e)}


    async def reporte_salarios_top(id_programa: int, top: int = 5):
        """
        Top N de egresados con mejores salarios en un programa.
        Devuelve solo idEgresado y salario (sin datos personales).
        """
        try:
            ids = obtener_ids_egresados_por_programa(id_programa)
            if not ids:
                return {"mensaje": "No hay egresados registrados para este programa"}

            situaciones = obtener_situacion_laboral_por_ids(ids)

            con_salario = [
                {"idEgresado": s["idEgresado"], "salario": float(s["salarioActual"])}
                for s in situaciones
                if s.get("estaEmpleado") and s.get("salarioActual")
            ]

            top_salarios = sorted(con_salario, key=lambda x: x["salario"], reverse=True)[:top]

            return {
                "idPrograma": id_programa,
                "top": top,
                "mejoresSalarios": top_salarios,
            }

        except Exception as e:
            return {"error": str(e)}