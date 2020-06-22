# Desafío 2
# Desarrollar una solución que calcule la suma de los cuadrados de los n primeros números naturales: 1 + 22 + 32 +… + n2.


tope = int(input("Ingrese un número tope: "))
sumatoria = 0
for num in range(1, tope + 1):
    sumatoria += num**2

print(f"La suma de los cuadrados de los primeros {tope} números naturales es {sumatoria}")
