import pymongo
from clases import farmaceutico
from guardarMongo import *
MONGO_HOST = "localhost"
MONGO_PUERTO = "27017"
MONGO_TIEMPO_FUERA=1000
MONGO_NOMBREDB = "db_Harmacia"
MONGO_NOMBRECOLECCION = "usuariosRegistrados"
MONGO_URI = "mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"
cliente = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
baseDatos = cliente[MONGO_NOMBREDB]
coleccion = baseDatos[MONGO_NOMBRECOLECCION] 
def guardarUsuario(documento):
    try:
        coleccion.insert_many(documento)
        print("Se ha guardao con éxito")
        return True
    except:
        print("No se ha logrado guardar")
        return False