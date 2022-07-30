import pandas as pd
import random as r
import time
from guardarMongo import guardarUsuario
data = pd.read_csv("datos.csv")
def obtenerDatosPorSeparados():
    '''
    def obtenerDatosPorSeparados():
        Funcion que obtiene los datos separados en diferentes  diccionarios
    '''
    nombres=[]
    apellidos=[]
    telefonos=[]
    direcciones=[]
    nombres = data["nombre"]
    apellidos = data["apellido"]
    telefonos= data["telefono"]
    direcciones = data["direccion"]
    return nombres, apellidos, telefonos, direcciones
def generarUsuarios(cantidadUsuarios):
    '''
    generarUsuarios(cantidadUsuarios):
        Funcion que genera N cantidad de usuarios en una coleccion, y luego es insertada en mongo db
    '''
    incio=time.time()  
    nombres=obtenerDatosPorSeparados()[0]
    apellidos=obtenerDatosPorSeparados()[1]
    telefonos=obtenerDatosPorSeparados()[2]
    direcciones=obtenerDatosPorSeparados()[3]
    diccionarios=[]
    for i in range(cantidadUsuarios):
        diccionarios.append({"nombre":nombres[r.randint(0,999)],"apellido":apellidos[r.randint(0,999)],"telefono":telefonos[r.randint(0,999)],"direccion":direcciones[r.randint(0,999)]})
    guardarUsuario(diccionarios)
    final=time.time() 
    print("Tiempo de ejecución:", final-incio)
generarUsuarios(3)




    