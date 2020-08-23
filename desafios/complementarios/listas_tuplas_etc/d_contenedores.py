# En un almacén se guarda mercadería en contenedores. 
# No es posible colocar más de n contenedores uno encima del otro y, 
# no hay área para más de 5 pilas de contenedores. 
# 
# Elabore un programa que permita gestionar el ingreso y salida de contenedores. 
# Note que para retirar un contenedor es necesario retirar los contenedores que están encima de él y colocarlos en otra pila.

import os


contenedores = {
    'a': [],
    'b': [],
    'c': [],
    'd': [],
    'e': [],
}



def mostrar_contenedores(contenedores):
    """Muestra el estado de los contenedores"""
    print(contenedores)

def agregar_contenedor(contenedor, pila):
    """Agrega un contenedor a la pila indicada"""
    pila.append(contenedor)

def quitar_contenedor(pila):
    """Quita un contenedor de la pila indicada"""
    return pila.pop()

def quitar_contenedor_por_nombre(contenedor_name, pila):
    pila_temporal = []
    for contenedor in pila[:]:
        if contenedor != contenedor_name:
            agregar_contenedor(pila_temporal, quitar_contenedor(pila))
        else:
            agregar_contenedor(pila)

def menu():
    mensaje = ''
    while True:
        menu_string = f"""
        1) Listar Contenedores
        2) Agregar Contenedor
        3) Quitar Contenedor

        {mensaje}
        """
        print(menu_string)
        opcion = input("Ingrese Opción: ")
        if len(opcion) == 1 and opcion in "123":
            mensaje = ""
            if opcion == '1':
                mostrar_contenedores(contenedores)
                menu()
            elif opcion == "2":
                nombre = input("Nombre del Contenedor: ")
                pila = input("Indicar la pila: ")
                agregar_contenedor(nombre, contenedores[pila])
                mostrar_contenedores(contenedores)
        else:
            os.system("cls")
            mensaje = "Intente otra vez, Nene"

if __name__ == "__main__":
    menu()
