# Hacer un programa que permita determinar todos los divisores de un número ingresado por el teclado.
from utils.myutils import continuar


while True:
    numero = int(input("Número: "))
    for n in range(1, numero):
        if numero % n == 0:
            print(f"{numero} es divisible por {n}")
    if continuar():
        continue
    else:
        break
