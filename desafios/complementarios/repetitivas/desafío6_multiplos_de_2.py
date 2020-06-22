# Desafío 6
# Imprimir, contar y sumar los múltiplos de 2 que hay entre una serie de números, 
# tal que el segundo sea mayor o igual que el primero.


num1 = int(input("Ingrese un número: "))
while True:
    num2 = int(input(f"Ingrese otro número: "))
    if num2 >= num1:
        break
    else:
        print(f"Aviso: Ingrese un número mayor o igual a {num1}: ")

cantidad_multiplos = 0
sumatoria = 0
for i in range(num1 + 1, num2):
    if i % 2 == 0:
        print(i)
        cantidad_multiplos += 1
        sumatoria += i

print(f"Se encontraron {cantidad_multiplos} múltiplos de 2, sumando {sumatoria}")
