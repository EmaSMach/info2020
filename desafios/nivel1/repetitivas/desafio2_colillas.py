# DESAFÍO 2
# Se inicia una campaña de recolección de colillas de cigarrillos en los barrios.

# Realizá un programa que permita registrar cantidad de colillas recolectadas por 
# un número determinado de personas. Luego obtener estadísticas al respecto 
# informando porcentaje de personas que han encontrado menos de 100 colillas,
#  más de 100 y menos de 200, más de 200 colillas.


total_colillas = 0
personas_100 = 0
personas_200 = 0
personas_300 = 0

print("Presione solo <Enter> sin ingresar nada para finalizar\n")
colillas = True
while colillas:
    colillas = input("Colillas: ")
    if colillas.isdigit():
        colillas = int(colillas)
        if colillas < 100:
            personas_100 += 1
            total_colillas += colillas
        elif 100 <= colillas < 200:  # colillas >= 100 and colillas < 200:
            personas_200 += 1
            total_colillas += colillas
        else:
            personas_300 += 1
            total_colillas += colillas
    else:
        colillas = False

print("\nESTADÍSTICAS")
print()
print("Total personas: ", personas_100 + personas_200 + personas_300)
print("Total colillas: ", total_colillas)
print()
total_personas = personas_100 + personas_200 + personas_300
print("Menos de 100 >>> ", 100*personas_100/total_personas if personas_100 else 0, "%")
print("De 100 a 199 >>> ", 100*personas_200/total_personas if personas_200 else 0, "%")
print("Desde 200    >>> ", 100*personas_300/total_personas if personas_300 else 0, "%")
