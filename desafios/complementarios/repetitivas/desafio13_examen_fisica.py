# Un grupo de 100 estudiantes presentan un exámen de Física. 
# Diseñe un diagrama que lea por cada estudiante la calificación obtenida y calcule e imprima:

# A.- La cantidad de estudiantes que obtuvieron una calificación menor a 50.

# B.- La cantidad de estudiantes que obtuvieron una calificación de 50 o más pero menor que 80.

# C.- La cantidad de estudiantes que obtuvieron una calificación de 70 o más pero menor que 80.

# D. La cantidad de estudiantes que obtuvieron una calificación de 80 o más.


estudiantes = 5
estudiantes_50 = 0
estudiantes_50_80 = 0
estudiantes_70_80 = 0
estudiantes_80 = 0

while estudiantes:
    nota = float(input("Nota: "))
    if nota < 50:
        estudiantes_50 += 1
    if nota >= 50:
        if 50 <= nota < 80:
            estudiantes_50_80 += 1
        if 70 <= nota < 80:
            estudiantes_70_80 += 1
        if nota >= 80:
            estudiantes_80 += 1
    estudiantes -= 1

print("Estudiantes menos de 50: ", estudiantes_50)
print("Estudiantes de 50 a 79: ", estudiantes_50_80)
print("Estudiantes de 70 a 79: ", estudiantes_70_80)
print("Estudiantes de 80 o más: ", estudiantes_80)