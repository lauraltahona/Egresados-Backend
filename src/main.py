from fastapi import FastAPI
from src.controller.usuario_controller import usuario_router
from src.controller.rol_controller import rol_router
from src.controller.login_controller import login_router
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
app.include_router(login_router)
