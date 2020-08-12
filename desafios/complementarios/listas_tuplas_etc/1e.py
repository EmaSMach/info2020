# Cargar m elementos en una pila, y luego copiarlos en una nueva lista.

pila = []

def apilar(lista, pila):
    for elemento in lista:
        pila.append(elemento)

def desapilar(lista, pila):
    for elemento in pila[::]:
        lista.append(pila.pop())

lista = [1, 2, 3, 4, 5]
apilar(lista, pila)
print(pila)
nueva_lista = pila.copy() # solo copiando, como dice el enunciado
print(nueva_lista)

# desapilando
lista_vacia = []
desapilar(lista_vacia, pila)
print(pila) # pila vacía
print(lista_vacia)