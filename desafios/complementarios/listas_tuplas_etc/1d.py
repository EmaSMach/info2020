# Realice una función que dada una lista de enteros L, y un número entero n. 
# Elimine de la lista original los elementos que sean iguales a ese número dado.


def modificando_L(L, n):
    for elem in L:
        if elem == n:
            L.remove(elem)
    return L

lista = [1, 2, 3, 4, 5, 3, 5]

print("Lista Original", lista)
print("Lista Modificada", modificando_L(lista, 3))
