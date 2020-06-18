# Desafío 3: Determinar si el primero de un conjunto de tres números dados, es menor que los otros dos.


numbers = []

while True:
    num = int(input("Ingrese un número: "))
    numbers.append(num)
    if len(numbers) == 3:
        break

print(numbers)
menor = numbers[0] == min(numbers)
if menor:
    print("El primer número es el menor")
else:
    print("El primer número no es el menor")

# Alternative form
num1 = None
num2 = None
num3 = None

limite = 0
while limite < 3:
    num = int(input("Ingrese un número: "))
    if limite == 0:
        num1 = num
    elif limite == 1:
        num2 = num
    else:
        num3 = num
    limite += 1

if num1 < num2 and num1 < num3:
    print("El primer número es el menor de todos")
else:
    print("El primer número no es el menor de todos")