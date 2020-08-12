# Construya un algoritmo que sume todos los elementos en posición par de una lista.

def sumar_pares(lista):
    """Suma elementos en posiciones pares (al ojo humano)"""
    suma = 0
    for pos, numero in enumerate(lista):
        if pos % 2 != 0:
            suma += numero
    return suma

print(sumar_pares(range(10))) 

