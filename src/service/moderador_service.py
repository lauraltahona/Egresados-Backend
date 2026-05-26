from fastapi import HTTPException
from src.provider.groq_provider import GroqProvider

class ModeracionService:

    @staticmethod
    def validar_contenido(texto: str):

        resultado = GroqProvider.analizar_contenido(texto)
        print(f"✅resultado: {resultado}")
        if not resultado["aprobado"]:

            raise HTTPException(
                status_code=400,
                detail=resultado["motivo"]
            )

        return True