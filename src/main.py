from fastapi import FastAPI
from src.controller.usuario_controller import usuario_router
from src.controller.rol_controller import rol_router
from src.controller.login_controller import login_router
from src.controller.facultad_controller import facultad_router
from src.controller.programa_controller import programa_router
from src.controller.beneficio_controller import beneficio_router
from src.controller.encuesta_controller import encuesta_router
from src.controller.preguntaEncuesta_controller import pregunta_encuesta_router
from src.controller.respuestaEncuesta_controller import respuesta_encuesta_router
from src.controller.proyecto_controller import proyecto_router
from src.controller.situacionLaboral_controller import situacion_router
from src.controller.egresado_controller import egresado_router
from src.controller.ofertaLaboral_controller import oferta_router
from src.controller.file_controller import file_router
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
app.include_router(facultad_router)
app.include_router(programa_router)
app.include_router(proyecto_router)
app.include_router(situacion_router)
app.include_router(beneficio_router)
app.include_router(egresado_router)
app.include_router(oferta_router)
app.include_router(file_router)
app.include_router(encuesta_router)
app.include_router(pregunta_encuesta_router)
app.include_router(respuesta_encuesta_router)




