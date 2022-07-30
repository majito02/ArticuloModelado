class farmaceutico():
    def __init__(self, id_farma, nombre, apellido):
        self.id_farma = id_farma
        self.nombre = nombre
        self.apellido = apellido
    def metodologin():
        print("gola")
class factura ():
    def __init__(self, id_factura, descripción, fecha, cantidad, total, id_farma, id_cliente, id_producto):
        self.id_factura = id_factura
        self.descripción = descripción
        self.fecha = fecha
        self.cantidad = cantidad
        self.total = total
        self.id_farma = id_farma
        self.id_cliente = id_cliente
        self.id_producto = id_producto
class cliente:
    def __init__(self, id_cliente, nombre, apellido, dirección):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.dirección = dirección
class producto():
    def __init__(self, id_producto, nombre, unidades_stock, id_categoria, id_proveedor):
        self.id_producto = id_producto
        self.nombre = nombre
        self.unidades_stock = unidades_stock
        self.id_categoria = id_categoria
class proveedor():
    def __init__(self, id_proveedor, nombre, apellido):
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.apellido = apellido



