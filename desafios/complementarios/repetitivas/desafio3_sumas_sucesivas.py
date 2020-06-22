# Desafio 3
# Diseñar un programa que permita obtener el producto entre A y B mediante sumas sucesivas.


num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))

producto = 0
for i in range(num1):
    producto += num2

print(f"{num1} x {num2} = {producto}")
