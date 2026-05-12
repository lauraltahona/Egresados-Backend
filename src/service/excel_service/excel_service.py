import io
from typing import Any

import pandas as pd
from fastapi import HTTPException
from fastapi.responses import StreamingResponse

def exportar_excel(datos: list[dict[str, Any]], nombre_hoja: str = "Datos") -> StreamingResponse:
    
    if not datos:
        raise HTTPException(status_code=404, detail="No hay datos para exportar")

    df = pd.DataFrame(datos)

    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name=nombre_hoja)

        hoja = writer.sheets[nombre_hoja]
        for col in hoja.columns:
            max_len = max(len(str(celda.value or "")) for celda in col)
            hoja.column_dimensions[col[0].column_letter].width = min(max_len + 4, 60)

    buffer.seek(0)
    nombre_archivo = f"{nombre_hoja.lower().replace(' ', '_')}.xlsx"

    return StreamingResponse(
        buffer,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": f"attachment; filename={nombre_archivo}"}
    )