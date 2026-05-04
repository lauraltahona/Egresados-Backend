import uuid
from fastapi import UploadFile
import os
from dotenv import load_dotenv
from src.config.supabase_client import supabase

load_dotenv()

class FileService:

    async def subir_imagen(archivo: UploadFile, carpeta: str = "general") -> str:
        try:
            contenido = await archivo.read()
            extension = archivo.filename.split(".")[-1]
            nombre_archivo = f"{carpeta}/{uuid.uuid4()}.{extension}"


            print(f"content_type: {archivo.content_type}")

            supabase.storage.from_("imagenes").upload(
                path=nombre_archivo,
                file=contenido,
                file_options={"content_type": archivo.content_type}
            )
            
            bucket_name = os.getenv("BUCKET_NAME_IMG")
            url = supabase.storage.from_(bucket_name).get_public_url(nombre_archivo)#.public_url
            return url
        
        except Exception as e:
            print(f"Error al subir la imagen: {e}")
            raise Exception("Error al subir la imagen")