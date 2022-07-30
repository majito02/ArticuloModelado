import pandas as pd
import random as r
data = pd.read_csv("cliente_antiguo.csv", sep=";")
c0 = []
c1 = []
c2 = []
c3 = []
c4 = []
c0 = data["id_cliente"]
c1 = data["nombre"]
c2 = data["apellido"]
c3 = data["telefono"]
c4 = data["direccion"]

# Obtener valores aleatorios de los datos del dataset y los guardar en una lista por cada columna
diccionarios = []
for i in range(500000): # Insertar medio millon de clientes
    diccionarios.append({"id_cliente": c0[r.randint(0, 999)], "nombre": c1[r.randint(0, 999)], "apellido": c2[r.randint(
        0, 999)], "telefono": c3[r.randint(0, 999)], "direccion": c4[r.randint(0, 999)]})


# Crear un dataframe con los valores aleatorios
df = pd.DataFrame(diccionarios)

# Guardar el dataframe en un archivo csv
df.to_csv("cliente.csv", sep=";")
