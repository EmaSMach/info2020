# Desarrolle un programa que permita determinar si un número X ingresado es par o impar.


def es_par(num):
    return num % 2 == 0


num1 = int(input("Ingrese número: "))
if es_par(num1):
    print("El número", num1, "es par")
else:
    print("El número", num1, "es impar")
