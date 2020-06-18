## Desafío 1: Solicite al usuario el ingreso de 3 números, e imprímalos de mayor a menor.


# numbers = []
# while True:
#     num = int(input("Ingrese número: "))
#     numbers.append(num)
#     if len(numbers) == 3:
#         break
# numbers = sorted(numbers, reverse=True)
# print("Mayor:", numbers[0])
# print("Medio:", numbers[1])
# print("Menor:", numbers[2])


# Alternative form
numeros_ingresados = 0
num1 = None
num2 = None
num3 = None
while numeros_ingresados < 3:
    num = int(input("Ingrese número: "))
    if numeros_ingresados == 0:
        num1 = num
    elif numeros_ingresados == 1:
        num2 = num
    else:
        num3 = num
    numeros_ingresados += 1

mayor = num1 if num1 > num2 and num1 > num3 else (num2 if num2 > num3 else num3)
menor = num1 if num1 < num2 and num1 < num3 else (num2 if num2 < num3 else num3)
medio = num1 if (mayor == num2 and menor == num3) or (mayor == num3 and menor == num2) else \
        num2 if (mayor == num1 and menor == num3) or (mayor == num3 and menor == num1) else num3

print("Mayor", mayor)
print("Medio", medio)
print("Menor", menor)
