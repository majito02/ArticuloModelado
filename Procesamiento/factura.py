import pandas as pd
import random as r
data=pd.read_csv("factura_antiguo.csv", sep=";")
c0 = []
c1 = []
c2 = []
c3 = []
c4 = []
c5 = []
c6 = []
c7 = []

c0=data["id_factura"]
c1 = data["descripcion"]
c2 = data["fecha"]
c3 = data["cantidad"]
c4 = data["total"]
c5 = data["id_farma"]
c6=data["id_cliente"]
c7=data["id_producto"]

#Obtener valores aleatorios de los datos del dataset y los guardar en una lista por cada columna
diccionarios=[]
for i in range(600000): #Insertar 600 mil registros de facturas
    diccionarios.append({"id_factura": c0[r.randint(1,999)],"descripcion":c1[r.randint(1,999)],"fecha":c2[r.randint(1,999)],"cantidad":c3[r.randint(1,999)],"total":c4[r.randint(1,999)],"id_farma":c5[r.randint(1,999)],"id_cliente":c6[r.randint(1,999)],"id_producto":c7[r.randint(1,999)]})
#Crear un dataframe con los valores aleatorios
df = pd.DataFrame(diccionarios)
#Guardar el dataframe en un archivo csv
df.to_csv("factura.csv", sep=";")




