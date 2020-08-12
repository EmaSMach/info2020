# Escriba un algoritmo que permita cargar una lista. 
# Y que luego, una vez cargada, controle y sustituya cualquier elemento negativo por 0


# List comprehension

lista = list(range(-5, 5))
print("Lista Original: ", lista)
zero_lista = [num if num >= 0 else 0 for num in lista]
print("Lista Modificada", zero_lista)

# modificando la lista original
lista2 = list(range(-5, 5))
for pos, elem in enumerate(lista2):
    if elem < 0:
        lista2[pos] = 0

print("Lista Modificada", lista2)