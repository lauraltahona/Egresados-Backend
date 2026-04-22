from fastapi import FastAPI
from src.controller.usuario_controller.usuario_controller_crud import usuario_router

app = FastAPI()

@app.get('/')
def health():
    return {"message": 'API is down!'}

app.include_router(usuario_router)