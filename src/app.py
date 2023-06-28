# Codigo sustraido del canal url=('https://youtu.be/FX0lMm_Qj10')
# creditos respectivos al autor y o su equipo de trabajo, "Repositorio=('https://github.com/UskoKruM/flask-login-mysql')"


# -----------------------------------------------------
# Sección donde importaremos Modulos, Instancias y variables, que utilizaresmos.
# -----------------------------------------------------
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required

import re

from config import config

# Models:
from models.ModelUser import ModelUser

# Entities:
from models.entities.User import User

from models.entities.User import *

#Para subir archivo tipo foto al servidor
from werkzeug.utils import secure_filename 

#El módulo os en Python proporciona los detalles y la funcionalidad del sistema operativo.
import os 

#Modulo para obtener la ruta o directorio
from os import path 

# -----------------------------------------------------
# Sección donde inicializaremos o definiremos las instancias principales.
# -----------------------------------------------------

# Constructor principal para ejecutar el sistema de información.
app = Flask(__name__)

# Para poder brindar seguridad extra, al usar tokens.
csrf = CSRFProtect()

# Para utilizar sentencias sql
db = MySQL(app)

# Para el control de vistas a usuarios no registrados.
login_manager_app = LoginManager(app)


# Función para poder hacer uso de las instancias de LoginManager.
@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)


# -----------------------------------------------------
# Sección principal de autentificación de usuario.
# -----------------------------------------------------


# Para definir la ruta y metodos por los que obtendremos los datos del login.
@app.route("/login", methods=["GET", "POST"])

# Función principal de login, que sera el pilar principal de todo nuestro sistema de información.
def login():
    # Este if principal reune el desarrollo principal en el que determinaremos las funcionalidades principales
    # como primero definir si tenemos los datos enviados por metodo POST
    if request.method == "POST":
        # print(request.form['NDI'])
        # print(request.form['password'])

        # Definir la instancia usuarios, la cual le pasamos los parametros del "NDI" y el "password".
        user = User(
            0, request.form["NDI"], request.form["password"], 0, 0, 0, 0, 0, 0, 0, 0, 0
        )

        # Funcion para comprovar el logged del usuario, osea verificar que es una cuenta existente.
        logged_user = ModelUser.login(db, user)

        # Siguiendo con la misma funcionalidad, tenemos la comprovación de que el usuario esta registrado
        # es certera, se procedera a realizar los siguientes if.
        if logged_user != None:
            # Este if nos comprueba si la contraseña sustraida, esta registrada o no, en la base de datos.
            if logged_user.password:
                login_user(logged_user)
                # En cuyo caso que el metodo de verificación nos comprueve que efectivamente es un usario y contraseña valida
                # se retornara a la vista que desea el usuario.
                return redirect(url_for("home"))
            else:
                # Caso contrario en que el usuario nos brinder una contraseña invalida pasaremos a indicarselo y redirigirnos
                # nuevamente al login principal.

                # Flash es un metodo que utilizamos para dar envio del mesaje a travez de un boton notificando lo indicado.
                flash("Contraseña invalida...")
                # Para dar retorno a nuestra ruta principal.
                return render_template("auth/login.html")
        # Caso en el que no encontremos que es un usuario registrado simplemente le indicaremos lo siguiente.
        else:
            # Usamos nuevamente el metodo para enviar mensaje donde indicamos al usuario que no se ha encontrado su usuario.
            flash("usuario no encontrado...")
            # Para dar retorno a nuestra ruta principal.
            return render_template("auth/login.html")
    # En caso de que el metodo no sea autentificado se realizara lo siguiente.
    else:
        # Para dar retorno a nuestra ruta principal.
        return render_template("auth/login.html")


# -----------------------------------------------------
# Sección principal de actualización de usuario.
# -----------------------------------------------------

@app.route("/edit", methods=["POST"])
def update():
    # Presentamos el bloque try, el cual pasara a ejecutar la sentencia "SQL".
    # try:
    #     # Definimos cursor para la sentencia SQL, la cual obtendremos todos los datos del usuario.
    #     cursor = db.connection.cursor()
    #     sql = "UPDATE user SET fullname = 'andragora' WHERE id = 1 "
    #     cursor.execute(sql)
    #     db.connection.commit()
    #     return render_template("profile/profile.html")
    # except Exception as ex:
    #     raise Exception(ex)


    # if name and numerodocumento:
    #     cursor = db.connection.cursor()
    #      #sql = "UPDATE user SET fullname = 'diomedes' WHERE NDI = 1 "
    #     sentencia = "UPDATE user SET fullname = (name) WHERE NDI = 1".format(name)
    #     cursor.execute(sentencia)
    #     db.connection.commit()
    # return render_template("profile/profile.html")


    # numerodocumento = request.form['NDI']    
    # name = request.form['fullname']
    # print(name, numerodocumento)
    # try:
    #     # Definimos cursor para la sentencia SQL, la cual obtendremos todos los datos del usuario.
    #     cursor = db.connection.cursor()
    #     sql = "UPDATE user SET fullname = '{}' WHERE NDI = 1".format(name)
    #     data = (name)
    #     cursor.execute(sql, data)
    #     db.connection.commit()
    #     print(request.form['NDI'])
    #     print(request.form['fullname'])
    #     return render_template("profile/profile.html")
    # except Exception as ex:
    #     raise Exception(ex)


    # numerodocumento = request.form['NDI']    
    # nombre = request.form['fullname']
    # try:
    #     # Definimos cursor para la sentencia SQL, la cual obtendremos todos los datos del usuario.
    #     cursor = db.connection.cursor()
    #     # sql = "UPDATE user SET fullname = 'narsiso' WHERE id = 1 "
    #     sql = (""" UPDATE login_python SET fullname = %s
    #             WHERE id = 1 """, (nombre, numerodocumento))
    #     cursor.execute(sql)
    #     db.connection.commit()
    #     print(request.form['NDI'])
    #     print(request.form['fullname'])
    #     return render_template("profile/profile.html")
    # except Exception as ex:
    #     raise Exception(ex)

    #--------------------------------------------------------------------------------------------------

    # Presentamos el bloque try, el cual pasara a ejecutar la sentencia "SQL".
    try:
        if request.method == 'POST':
            if(request.files['archivo']):

                NumDoc = request.form['NDI']

                #Script para archivo
                nombreArchivo = NumDoc
                file     = request.files['archivo']
                basepath = path.dirname (__file__) #La ruta donde se encuentra el archivo actual
                
                #capturando extensión del archivo ejemplo: (.png, .jpg, .pdf ...etc)
                extension           = ('.jpg')
                nuevoNombreFile     = nombreArchivo + extension
        
                upload_path = path.join (basepath, 'static/img/avatars', nuevoNombreFile) 
                file.save(upload_path)

                # Definimos cursor con la conexión de la based de datos para poder realizar la consulta.
                cursor = db.connection.cursor()
                # Veremos la siguiente consultaa de tipo UPDATE, en el que le pasamos los parametros para insertar los datos que deseamos actualizar.
                sql="""UPDATE users SET Nombre_img = '{1}'  WHERE NDI = {0}"""

                Atr = (NumDoc, nuevoNombreFile)

                # Usamos el execute para poder realizar la consulta anteriormente mostrada.
                cursor.execute(sql.format(Atr[0],Atr[1]))

                # sql = "UPDATE user SET fullname = 'mandragora' WHERE id = 1 "

                # cursor.execute(sql)
                db.connection.commit()
                
        # Definimos todos los paremtros que recolectamos del formulario, y definimos una variable para utilizar 
        # los datos en la consulta posterior de MySql.
        nombre= request.form['fullname']
        direccion= request.form['Direccion']
        Telefono = request.form['Telefono']
        Empresa = request.form['Empresa']
        Cargo = request.form['Cargo']
        Area = request.form['Area']
        Fecha_nacimiento = request.form['FDN']
        NumDoc = request.form['NDI']
        Email = request.form['Email']

        # Definimos un array llamado curso para poder utilizar las vriables anteriormente definidas.
        curso = (nombre, direccion, Telefono, Empresa, Cargo, Area, Fecha_nacimiento, NumDoc, Email)

        # Definimos cursor con la conexión de la based de datos para poder realizar la consulta.
        cursor = db.connection.cursor()
        # Veremos la siguiente consultaa de tipo UPDATE, en el que le pasamos los parametros para insertar los datos que deseamos actualizar.
        sql="""UPDATE users SET fullname = '{0}', Direccion = '{1}', Telefono= '{2}', Empresa= '{3}', Cargo= '{4}', 
                Area_locativa= '{5}', Fecha_nacimiento = '{6}', NDI= '{7}', Email= '{8}' WHERE NDI = {7}"""
        # Usamos el execute para poder realizar la consulta anteriormente mostrada.
        cursor.execute(sql.format(curso[0],curso[1],curso[2],curso[3],curso[4],curso[5],curso[6],curso[7],curso[8]))
        # sql = "UPDATE user SET fullname = 'mandragora' WHERE id = 1 "
        # cursor.execute(sql)
        db.connection.commit()

        return render_template("profile/profile.html")
    except Exception as ex:
         raise Exception(ex)
    

# -----------------------------------------------------
# Apartado de las rutas principales con sus respectivas caracteristicas.
# -----------------------------------------------------


# Para incializar el sistema de información con la ruta indicada.
@app.route("/")
def index():
    return redirect(url_for("login"))


# -----------------------------------------------------
# Ruta de login principal
@app.route("/logout")
# Utilizamos esta función para cerrar sesión del usuario y volver a login principal
# osea que para dirigirnos a la ruta del login, reflejaremos el cerrar sesión del usuario.
def logout():
    logout_user()
    return redirect(url_for("login"))


# -----------------------------------------------------
# Ruta de home donde nos llevara a la hora de realizar la verificación de usuario.
@app.route("/home")
# Utilizamos el metodo de login_required para proteger esta ruta y exigir que se inicie sesión
# de manera obligatoria para acceder a esta, y no poder hacerlo encontrando la ruta.
@login_required
def home():
    return render_template("home.html")


# -----------------------------------------------------
# Ruta de home donde nos llevara a la hora de realizar la verificación de usuario.
@app.route("/profile")
# Utilizamos el metodo de login_required para proteger esta ruta y exigir que se inicie sesión
# de manera obligatoria para acceder a esta, y no poder hacerlo encontrando la ruta.
@login_required
def profile():
    return render_template("profile/profile.html")


# -----------------------------------------------------
# Ruta de home donde nos llevara a la hora de realizar la verificación de usuario.
@app.route("/help")
# Utilizamos el metodo de login_required para proteger esta ruta y exigir que se inicie sesión
# de manera obligatoria para acceder a esta, y no poder hacerlo encontrando la ruta.
@login_required
def help():
    return render_template("help/help.html")


# -----------------------------------------------------
# Apartado de las funciones de los errores
# -----------------------------------------------------


# Error en el que el usuario quiere acceder a una ruta que posee el "Login_requeried"
# el cual lo redigira a la ruta login principal.
def status_401(error):
    return redirect(url_for("login"))


# Error en el que el usuario intenta accesar a una ruta invalida o incorrecta.
def status_404(error):
    return "<h1>Pagina no encontrada :(...<h1/>", 404


# -----------------------------------------------------
# Apartado de inicialización del proyecto.
# -----------------------------------------------------
if __name__ == "__main__":
    app.config.from_object(config["development"])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run()
