from fastapi import FastAPI
from src.controller.usuario_controller.usuario_controller_crud import usuario_router
from src.controller.rol_controller.rol_controller_crud import rol_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Permite todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],      # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],      # Permite todos los headers
)


app = FastAPI()

@app.get('/')
def health():
    return {"message": 'API is down!'}

app.include_router(usuario_router)
app.include_router(rol_router)
