
#-----------------------------------------------------
#Sección donde importaremos Modulos, Instancias y variables, que utilizaresmos.
#-----------------------------------------------------
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

#Definimos la clase user, con los parametros de userMixin, para autentificar aal usuario.
class User(UserMixin):
    #Utilizamos el metodo __init__, para poder instanciar la función de manera rapida y facil.

    #Esta función nos brinda la recopilación de los atributos del usuario.
    def __init__(self, id, NDI, password, fullname, Direccion, Telefono, Empresa, Cargo, Area_locativa, Email, Fecha_nacimiento, Nombre_img = "" ) -> None:
        #  Direccion, Telefono, Empresa, Cargo, Area_locativa, Email, Fecha_nacimiento
        self.id = id
        self.NDI = NDI
        self.password = password
        self.fullname = fullname
        self.Direccion = Direccion
        self.Telefono = Telefono
        self.Empresa = Empresa
        self.Cargo = Cargo
        self.Area = Area_locativa
        self.Email = Email
        self.Fecha_nacimiento = Fecha_nacimiento
        self.Nombre_img = Nombre_img

    #Para realizar la verificación y comprovación del hash
    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)

#print(generate_password_hash("holabb"))
#pbkdf2:sha256:600000$4KEC0m5pbovSRyDe$2a3cc99f49180b6c63acfa1126ef7ced7c8554ad9112f1aff2a58ded9b25000c
#pbkdf2:sha256:600000$RmJkvDljtnXNGrSM$8c36155079b871e820f0d70c83458edaacaa9535fca958fcfb3fbfb0639ffeba