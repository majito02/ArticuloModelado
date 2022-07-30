import pandas as pd
import random as r

data=pd.read_csv("proveedor_antiguo.csv", sep=";")
c0 = []
c1 = []
c2 = []

c0=data["id_proveedor"]
c1=data["nombre"]
c2=data["nombre_responsable"]

#Obtener valores aleatorios de los datos del dataset y los guardar en una lista por cada columna
diccionarios=[]
for i in range(100000): #Insertar 1 millon de productos
    diccionarios.append({"id_proveedor": c0[r.randint(1,999)],"nombre":c1[r.randint(1,999)],"nombre_responsable":c2[r.randint(1,999)]})
#Crear un dataframe con los valores aleatorios
df = pd.DataFrame(diccionarios)
#Guardar el dataframe en un archivo csv
df.to_csv("proveedor.csv", sep=";")