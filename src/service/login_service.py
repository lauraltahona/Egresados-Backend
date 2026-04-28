import datetime
from src.config.supabase_client import supabase
import src.modelDto.usuario_dto as usuarioDto

class login:
    def __init__(self):
        pass
    
    async def Login(usuario: usuarioDto.UsuarioLogin):
        try:
            response = await supabase.auth.sign_in_with_password({
                "email": usuario.correo,
                "password": usuario.contrasena
            })
            
            usuarioLogin = await supabase.table("Usuarios")\
            .select("idusuario, nombreUsuario, apellidoUsuario, correo, celular, idRol, fechaRegistoUsuario")\
            .eq("id", response.user.id)\
            .single()\
            .execute()

            return {
                "token": response.session.access_token,
                "refresh_token": response.session.refresh_token,
                "user": usuarioLogin.data
            }
            
        except Exception as e:
            return {"error": str(e)}
        
    async def register(usuario: usuarioDto.UsuarioRegister):
        try:
            
            auth_response = supabase.auth.sign_up({
                "email": usuario.correo,
                "password": usuario.contrasena
            })

            if not auth_response.user:
                return {"error": "No se pudo crear el usuario"}
            
            usuarioRegister = {
                "idUsuario": auth_response.user.id,
                "nombreUsuario": usuario.nombreUsuario,
                "apellidoUsuario": usuario.apellidoUsuario,
                "correo": usuario.correo,
                "celular": usuario.celular,
                "idRol": usuario.idRol,
                "fechaRegistoUsuario": datetime.datetime.now().isoformat()
            }

            await supabase.table("Usuarios").insert(usuarioRegister).execute()

            return {
                "Mensaje": "Usuario registrado correctamente",
                "id": auth_response.user.id,
                "email": usuario.correo
            }

        except Exception as e:
            return {"error": str(e)}