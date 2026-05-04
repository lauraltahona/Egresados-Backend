from src.service.file_service import FileService
from fastapi import APIRouter, UploadFile, File

file_router = APIRouter(prefix="/files", tags=["files"])

@file_router.post("/upload-image")
async def subir_imagen_endpoint(imagen: UploadFile = File(...)):
    try:
        url = await FileService.subir_imagen(imagen, carpeta="ofertas")
        return {"imagenUrl": url}
    except Exception as e:
        return {"error": str(e)}
