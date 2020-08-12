# Cargue dos listas, y actualice la primer lista con los elementos que están en la segunda y no en la primera.

lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [5, 6, 7, 8, 9]

print(list(set(lista1 + lista2)))

# otro modo, modificando la lista original: lista1
for elemento in lista2:
    if elemento not in lista1:
        lista1.append(elemento)

print(lista1)