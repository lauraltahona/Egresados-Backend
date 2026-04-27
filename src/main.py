from fastapi import FastAPI
from src.controller.usuario.usuario_controller import usuario_router
from src.controller.rol.rol_controller import rol_router
from fastapi import FastAPI
from src.middleware.cors import setup_cors

app = FastAPI()

# middleware
setup_cors(app)

# api
@app.get('/')
def health():
    return {"message": 'API is up!'}

app.include_router(usuario_router)
app.include_router(rol_router)
