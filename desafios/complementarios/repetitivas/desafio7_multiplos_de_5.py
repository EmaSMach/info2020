# Desafiío 7
# Realizar un programa que calcule y muestre la suma de los múltiplos de 5 comprendidos entre dos valores A y B. 
# El programa no permitirá introducir valores negativos para A y B y verificará que A es menor que B. 
# Si A es mayor que B, se deben intercambiar los valores.


while True:
    num1 = int(input("Ingrese un número positivo: "))
    if num1 >= 0:
        break
    else:
        print("No se permiten números negativos, intente otra vez")
while True:
    num2 = int(input("Ingrese un segundo número: "))
    if num2 >= 0:
        break
    else:
        print("No se permiten números negativos, intente otra vez")

sumatoria = 0
a = num1 if num1 < num2 else num2
b = num1 if num1 > num2 else num2

for i in range(a, b):
    if i % 5 == 0:
        print(i)
        sumatoria += i

print("Sumatoria: ", sumatoria)
