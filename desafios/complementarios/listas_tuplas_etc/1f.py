# Cargar k elementos en una cola, y luego copiarlos en una nueva lista.

def acolar(lista, cola):
    for elem in lista:
        cola.insert(0, elem)

def desacolar(lista, cola):
    for elem in cola[:]:
        lista.append(cola.pop())

lista = [1, 2, 3, 4, 5]
cola = []
acolar(lista, cola) # carga los números empezando por el elemento en la primera posición
print(cola)         # por eso el primero quedó último
cola_copiada = cola.copy() # copiando
print(cola_copiada)

salida = []
desacolar(salida, cola) # empieza a quitar elementos empezando por el primero que entró, o sea el 1
print(salida)