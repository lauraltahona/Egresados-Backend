import json
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

class GroqProvider:

    @staticmethod
    def analizar_contenido(texto: str):

        prompt = f"""
        Analiza el siguiente texto.

        Responde SOLO en formato JSON válido:

        {{
            "aprobado": true,
            "motivo": "El texto tiene contenido no apropiado"
        }}

        Rechaza si contiene:
        - insultos
        - odio
        - amenazas
        - lenguaje ofensivo
        - acoso

        Texto:
        "{texto}"
        """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )

        contenido = response.choices[0].message.content.strip()

        contenido = contenido.replace("```json", "").replace("```", "").strip()

        print(f"✅contenido limpio: {contenido}")
        
        return json.loads(contenido)