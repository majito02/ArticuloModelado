# Insertar datos en monogodb con pandas
import pandas as pd
import time
import pymongo

inicio=time.time() 
# Cargar el dataframe
farma = pd.read_csv(
    "C:/dataset/CreacionRegistros/Procesamiento/csv/farmaceutico.csv", sep=";")
prov = pd.read_csv(
    "C:/dataset/CreacionRegistros/Procesamiento/csv/proveedor.csv", sep=";")
cli = pd.read_csv(
    "C:/dataset/CreacionRegistros/Procesamiento/csv/cliente.csv", sep=";")
cat = pd.read_csv(
    "C:/dataset/CreacionRegistros/Procesamiento/csv/categoria.csv", sep=";")
prod = pd.read_csv(
    "C:/dataset/CreacionRegistros/Procesamiento/csv/producto.csv", sep=";")
fact = pd.read_csv(
    "C:/dataset/CreacionRegistros/Procesamiento/csv/factura.csv", sep=";")


# Crear una conexion con mongo db
client = pymongo.MongoClient("mongodb://localhost:27017/")
# Utilizar la base de datos farmacia
db = client.farmacia
# Crear colecciones
farmaceutico = db.farmaceutico
proveedor = db.proveedor
cliente = db.cliente
categoria = db.categoria
producto = db.producto
factura = db.factura


# Obtener los datos de farmaceutico
nombres = farma["nombre"]
apellidos = farma["apellido"]
diccionario1 = []

# Obtener los datos de proveedor
nombres_proveedor = prov["nombre"]
nombre_resposable = prov["nombre_responsable"]
diccionario2 = []

# Obtener los datos de cliente
nombres_cliente = cli["nombre"]
apellidos_cliente = cli["apellido"]
telefono = cli["telefono"]
direccion = cli["direccion"]
diccionario3 = []

# Obtener los datos de categoria
catego = cat["categoria"]
diccionario4 = []

# Obtener los datos de producto
nombre_producto = prod["nombre"]
unidades_stock = prod["unidades_stock"]
id_categoria = prod["id_categoria"]
id_proveedor = prod["id_proveedor"]
diccionario5 = []

# Obtener los datos de factura
descripcion = fact["descripcion"]
fecha = fact["fecha"]
cantidad = fact["cantidad"]
total = fact["total"]
id_farma = fact["id_farma"]
id_cliente = fact["id_cliente"]
id_producto = fact["id_producto"]
diccionario6 = []


# Contar el numero de registros del dataset
conteoFarma = len(farma)
conteoProveedor = len(prov)
conteoCliente = len(cli)
conteoCategoria = len(cat)
conteoProducto = len(prod)
conteoFactura = len(fact)

# Insertar los datos en las colecciones

i = 1  # Contador

# Diccionario para guardar los datos de farmaceutico
for i in range(conteoFarma):
    diccionario1.append(
        {"_id": i, "nombre": nombres[i], "apellido": apellidos[i]})

# Diccionario para guardar los datos de proveedor
for i in range(conteoProveedor):
    diccionario2.append(
        {"_id": i, "nombre": nombres_proveedor[i], "nombre_responsable": nombre_resposable[i]})

# Diccionario para guardar los datos de cliente
for i in range(conteoCliente):
    diccionario3.append(
        {"_id": i, "nombre": nombres_cliente[i], "apellido": apellidos_cliente[i], "telefono": telefono[i], "direccion": direccion[i]})

# Diccionario para guardar los datos de categoria
for i in range(conteoCategoria):
    diccionario4.append({"_id": i, "categoria": catego[i]})

# Diccionario para guardar los datos de producto
for i in range(conteoProducto):
    diccionario5.append({"_id": i, "nombre": nombre_producto[i], "unidades_stock": unidades_stock[i],
                        "id_categoria": id_categoria[i], "id_proveedor": id_proveedor[i]})

# Diccionario para guardar los datos de factura
for i in range(conteoFactura):
    diccionario6.append({"_id": i, "descripcion": descripcion[i], "fecha": fecha[i], "cantidad": cantidad[i],
                        "total": total[i], "id_farma": id_farma[i], "id_cliente": id_cliente[i], "id_producto": id_producto[i]})


# Insertar los datos en las colecciones
farmaceutico.insert_many(diccionario1)
proveedor.insert_many(diccionario2)
cliente.insert_many(diccionario3)
categoria.insert_many(diccionario4)
producto.insert_many(diccionario5)
factura.insert_many(diccionario6)


#Tiempo de ejeucion
final = time.time()
print("\nTiempo de ejecucion: ", final - inicio)

# Terminar la conexion con mongo db
client.close()









