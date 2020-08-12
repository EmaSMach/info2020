# Realizar un algoritmo que invierta el orden de una cola.


def invertir_cola(cola: list):
    """Invierte el orden de la cola (lista)"""
    a = -1 # útlimo elemento
    b = 0  # primer elemento
    for elemento in cola[:]:
        elemento = cola.pop(-1)
        cola.insert(b, elemento)
        a -= 1
        b += 1
    return cola

cola = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(cola)
print(invertir_cola(cola))