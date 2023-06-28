
#-----------------------------------------------------
#Sección donde importaremos Modulos, Instancias y variables, que utilizaresmos.
#-----------------------------------------------------
from .entities.User import *

#-----------------------------------------------------
#Sección de la clase principal donde realizaremos las consultas requeridas por medio de bloques.
#-----------------------------------------------------
class ModelUser():
    #Usamos el decorador siguiente para poder utilizar las propiedades a la hora de llamarlas en el archivo"app".
    @classmethod
    #definimos login con los parametros necesarios para realizar la consulta pertinente.
    def login(self,db,user):
        #Presentamos el bloque try, el cual pasara a ejecutar la sentencia "SQL".
        try:
            #Definimos cursor para la sentencia SQL, la cual obtendremos todos los datos del usuario.
            cursor=db.connection.cursor()
            sql="""SELECT id_user, NDI, password, fullname, Direccion, Telefono, Empresa, Cargo, Area_locativa, Email, fecha_nacimiento, Nombre_img FROM users
                    WHERE NDI = '{}' """.format(user.NDI)    
            cursor.execute(sql)
            row=cursor.fetchone()

            #Aqui tenemos la condicional if con la que determinamos, si la variable row no esta vacia
            #se realizara lo siguiente.
            if row != None:
                #Definimos arrow como una lista en la posición indicada, que corresponde a los atributos
                #del usuario, anteriormente consultados.
                user=User(row[0],row[1],User.check_password(row[2],user.password),row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11])
                #Para retornar la lista con los datos.
                return user
            else:
                #En caso de no cumplirse la condición, no se retornaara ningún valor.
                return None
        except Exception as ex:
            raise Exception(ex)
        
    #Usamos el decorador siguiente para poder utilizar las propiedades a la hora de llamarlas en el archivo"app".
    @classmethod
    def get_by_id(self,db,id):
        #Presentamos el bloque try, el cual pasara a ejecutar la sentencia "SQL".
        try:
            #Definimos cursor, para realizar la siguiente consulta, donde sustraeremos el id del usuario.
            cursor=db.connection.cursor()
            sql="""SELECT id_user, NDI, fullname, Direccion, Telefono, Empresa, Cargo, Area_locativa, Email, Fecha_nacimiento, Nombre_img FROM users
                    WHERE id_user = '{}' """.format(id)    
            cursor.execute(sql)
            #Especificamos el metodo feetchone, el cual nos permite manetener la difeerencia y conservación 
            #de las mayusculas y minusculas.
            row=cursor.fetchone()

            #De igual manera para este bloque, se debe determinar la condicional que pondra en analisis 
            #el array con los datos del usuario.
            if row != None:
                return User(row[0],row[1],None,row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])
            else:
                return None
        #se utiliza except para dar fin al bloqué.
        except Exception as ex:
            raise Exception(ex)
        
   