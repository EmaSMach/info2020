# Desafío 18
# Se leen tres números que son las longitudes de los lados de un triángulo. 
# Determinar e informar si el mismo es equilátero (3 lados iguales), 
# isósceles (2 lados iguales) o escaleno (3 lados distintos).


lado1 = float(input("Lado 1: "))
lado2 = float(input("Lado 2: "))
lado3 = float(input("Lado 3: "))

if lado1 == lado2 == lado3:
    print("Triángulo Equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Triángulo Isóceles")
else:
    print("Triángulo Escaleno")
