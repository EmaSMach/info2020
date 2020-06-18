# Desafío 11
# Determinar si un alumno aprueba a reprueba un curso, 
# sabiendo que aprobara si su promedio de tres calificaciones es mayor o igual a 70; 
# desaprueba en caso contrario.


nota1 = int(input("Nota 1: "))
nota2 = int(input("Nota 2: "))
nota3 = int(input("Nota 3: "))

total = nota1 + nota2 + nota3

if total/3 >= 70:
    print("APROBADO!!", "su promedio es de ", total/3)
else:
    print("DESAPROBADO!!", "su promedio es de ", total/3)
