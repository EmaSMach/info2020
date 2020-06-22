# Desafío 1
# Determinar el número mayor de 10 números ingresados.


numeros = []
for i in range(10):
    ingreso = int(input("Ingrese un número: "))
    numeros.append(ingreso)

print(f"El mayor número es {max(numeros)}")
