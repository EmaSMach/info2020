# Desafío 5
# Solicitar el ingreso de números al usuario y emitir un mensaje para determinar si es par o impar.
# El ciclo debe finalizar cuando el usuario ingresa 0.


while True:
    num = int(input("Ingrese un número, o 0 para salir: "))
    if num == 0:
        break
    else:
        if num % 2 == 0:
            print(f"El número {num} es par")
        else:
            print(f"El número {num} es impar")
