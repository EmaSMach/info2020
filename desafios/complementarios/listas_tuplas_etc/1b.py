# Haz un programa que almacene 5 elementos en una variable del tipo lista, 
# la modiﬁque para que cada componente sea igual al cuadrado del componente original. 
# El programa mostrara la lista resultante por pantalla.


# list comprehension
lista = [1, 2, 3, 4, 5]

lista_al_cuadrado = [num**2 for num in lista]
print(lista_al_cuadrado)

# Modificando la lista original
lista2 = [1, 2, 3, 4, 5]
for pos, num in enumerate(lista):
    lista2[pos] = lista2[pos]**2

print(lista2)

