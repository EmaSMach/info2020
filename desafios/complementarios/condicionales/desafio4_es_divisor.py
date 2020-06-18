# Desafío 4: Realizar un programa que sea capaz de, habiéndose ingresado dos números m y n, determine si n es divisor de m.


num1 = int(input("Primer número: "))
num2 = int(input("Segundo número: "))

if num1 % num2 == 0:
    print(f"{num2} es divisor de {num1}")
else:
    print(f"{num2} no es divisor de {num1}")
