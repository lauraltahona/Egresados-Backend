from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

def setup_cors(app: FastAPI):
    app.add_middleware(
        CORSMiddleware, 
        allow_origins=["*"],      # Permite todos los orígenes
        allow_credentials=True,
        allow_methods=["*"],      # Permite todos los métodos (GET, POST, etc.)
        allow_headers=["*"],      # Permite todos los header)
    )
