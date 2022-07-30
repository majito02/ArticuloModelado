import pandas as pd
import random as r
data = pd.read_csv("producto_antiguo.csv", sep=";")
c0 = []
c1 = []
c2 = []
c3 = []
c4 = []
c0 = data["id_producto"]
c1 = data["nombre"]
c2 = data["unidades_stock"]
c3 = data["id_categoria"]
c4 = data["id_proveedor"]
# Obtener valores aleatorios de los datos del dataset y los guardar en una lista por cada columna
diccionarios = []
for i in range(1000000):  # Insertar 1 millon de productos
    diccionarios.append({"id_producto": c0[r.randint(1, 999)], "nombre": c1[r.randint(1, 999)], "unidades_stock": c2[r.randint(
        1, 999)], "id_categoria": c3[r.randint(1, 999)], "id_proveedor": c4[r.randint(1, 999)]})
# Crear un dataframe con los valores aleatorios
df = pd.DataFrame(diccionarios)
# Guardar el dataframe en un archivo csv
df.to_csv("producto.csv", sep=";")
