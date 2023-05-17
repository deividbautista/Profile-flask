#-----------------------------------------------------
#El presente archivo se utiliza para la conexión de base de datos.
#-----------------------------------------------------

#-----------------------------------------------------
#Apartado donde daremos configuración a la secret key.
#-----------------------------------------------------
class Config:
    SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'

#-----------------------------------------------------
#Apartado en el que se configura los datos del usuario.
#-----------------------------------------------------

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'profile-flask'

#-----------------------------------------------------
#Apartado de para definir la configuración general de la base de datos.
#-----------------------------------------------------

config={
    'development':DevelopmentConfig
}
