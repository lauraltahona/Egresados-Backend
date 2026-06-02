import datetime
from http.client import HTTPException
from src.config.supabase_client import supabase, supabase_admin
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
            .select("idUsuario, nombreUsuario, apellidoUsuario, correo, celular, idRol, Roles(nombreRol)")\
            .eq("idUsuario", response.user.id)\
            .single()\
            .execute()

            datos_usuario = usuarioLogin.data

            nombre_rol = datos_usuario.get("Roles", {}).get("nombreRol", "")
            if nombre_rol == "Egresado":
                egresado = supabase.table("Egresados")\
                    .select("idEgresado")\
                    .eq("correoEgresado", usuario.correo)\
                    .single()\
                    .execute()
                datos_usuario["idEgresado"] = egresado.data["idEgresado"] if egresado.data else None

            return {
                "token": response.session.access_token,
                "refresh_token": response.session.refresh_token,
                "usuario": datos_usuario
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
                raise HTTPException(status_code=400, detail="El correo ya está registrado")
            
            rol = supabase.table("Roles") \
            .select("nombreRol") \
            .eq("idRol", usuario.idRol) \
            .single() \
            .execute()

            authResponse = supabase_admin.auth.admin.create_user({
                "email": usuario.correo,
                "password": usuario.contrasena,
                "email_confirm": True
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
                "fechaRegistroUsuario": datetime.datetime.now().isoformat()
            }

            supabase.table("Usuarios").insert(usuarioRegister).execute()

            return {
                "id": authResponse.user.id,
                "email": usuario.correo
            }

        except Exception as e:
            return {"error": str(e)}
        
    async def cambiar_contrasena(usuario_id: str, contrasena_actual: str, nueva_contrasena: str):
        try:
            usuario = supabase.table("Usuarios") \
                .select("correo") \
                .eq("idUsuario", usuario_id) \
                .single() \
                .execute()
 
            if not usuario.data:
                return {"error": "Usuario no encontrado"}
 
            correo = usuario.data["correo"]
            
            verificacion = supabase.auth.sign_in_with_password({
                "email": correo,
                "password": contrasena_actual
            })
 
            if not verificacion.user:
                return {"error": "La contraseña actual es incorrecta"}
 
            supabase_admin.auth.admin.update_user_by_id(
                usuario_id,
                {"password": nueva_contrasena}
            )
 
            return {"mensaje": "Contraseña actualizada correctamente"}
 
        except Exception as e:
            return {"error": str(e)}