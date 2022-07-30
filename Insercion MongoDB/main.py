from ScriptGenerarNUsuarios import *
from guardarMongo import *
if __name__=="__main__":
    print("-----------------------------------------------------")
    print("               MENÚ PRINCIPAL")
    print("-----------------------------------------------------")
    print("Ingrese 1..........: Para registrar N clientes")
    print("Ingrese 2..........: Para Salir")
    opcion=int(input("Ingrese su opción: "))
    if opcion==1:
        cantidadUsuarios=int(input("Cuántos Usuarios desea registrar: "))
        generarUsuarios(cantidadUsuarios)
    elif opcion==2:
        print("-----------------------------------------------------")
        print("       Gracias por usar nuestro sistema")
        print("-----------------------------------------------------")



