# Desafío 1
# Escribir un programa que pregunte a diferentes personas
# cuánto conocen sobre contaminación del 1 al 10,
# almacene estos valores un una lista y los muestre por pantalla
# ordenados de menor a mayor.


print("¿Cuánto conoce sobre contaminación, del 1 al 10?")
lista_conocimiento = []
while True:
    conocimiento = input("Nivel de conocimiento (del 1 al 10) o <Enter> para terminar: ")
    if conocimiento:
        if conocimiento.isdigit():
            conocimiento = int(conocimiento)
            if conocimiento in range(1, 11):
                lista_conocimiento.append(conocimiento)
            else:
                print("AVISO: Ingrese solo números del 1 al 10")
        else:
            print("AVISO: Ingrese solo números")
    else:
        print("Terminado...")
        break

print()
print("Números ordenados:")
for elemento in sorted(lista_conocimiento):
    print(elemento)
