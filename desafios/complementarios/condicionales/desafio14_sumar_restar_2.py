# Desafío 14
# Leer 2 números; si son iguales que los multiplique, si el primero es mayor que el segundo que los reste y si no que los sume.


num1 = int(input("Numero 1: "))
num2 = int(input("Número 2: "))

if num1 == num2:
    print("Multiplicando: ", num1 * num2)
elif num1 > num2:
    print("Restando: ", num1 - num2)
else:
    print("Sumando: ", num1 + num2)
