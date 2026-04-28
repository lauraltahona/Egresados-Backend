import datetime
from src.config.supabase_client import supabase
import src.modelDto.usuario_dto as usuarioDto

class loginService:
    def __init__(self):
        pass
    
    async def Login(usuario: usuarioDto.UsuarioLogin):
        try:
            response = supabase.auth.sign_in_with_password({
                "email": usuario.correo,
                "password": usuario.contrasena
            })
            
            usuarioLogin = supabase.table("Usuarios")\
            .select("idUsuario, nombreUsuario, apellidoUsuario, correo, celular, idRol, fechaRegistoUsuario")\
            .eq("idUsuario", response.user.id)\
            .single()\
            .execute()

            return {
                "token": response.session.access_token,
                "refresh_token": response.session.refresh_token,
                "usuario": usuarioLogin.data
            }
            
        except Exception as e:
            return {"error": str(e)}
        
    async def register(usuario: usuarioDto.UsuarioRegister):
        try:
            
            existeUsuario = supabase.table("Usuarios")\
                    .select("idUsuario")\
                    .eq("correo", usuario.correo)\
                    .execute()
                
            if existeUsuario.data:
                return {"error": "El correo ya está registrado"}
            
            authResponse = supabase.auth.sign_up({
                "email": usuario.correo,
                "password": usuario.contrasena
            })

            if not authResponse.user:
                return {"error": "No se pudo crear el usuario"}
            
            usuarioRegister = {
                "idUsuario": authResponse.user.id,
                "nombreUsuario": usuario.nombreUsuario,
                "apellidoUsuario": usuario.apellidoUsuario,
                "correo": usuario.correo,
                "celular": usuario.celular,
                "idRol": usuario.idRol,
                "fechaRegistoUsuario": datetime.datetime.now().isoformat()
            }

            supabase.table("Usuarios").insert(usuarioRegister).execute()

            return {
                "Mensaje": "Usuario registrado correctamente",
                "id": authResponse.user.id,
                "email": usuario.correo
            }

        except Exception as e:
            return {"error": str(e)}