# Desafío 17
# Determinar y exhibir si la estatura de una persona adulta dada, 
# es mayor que la estatura media de las personas adultas de su sexo, siendo:

# - estatura media de mujeres adultas: 1,65 m.

# - estatura media de varones adultos: 1,72 m.


estatura = float(input("Estatura: "))
while True:
    sexo = input("Sexo (m/f): ").lower()
    if sexo in 'fm':
        break
    else:
        print("Opción no válida, intente otra vez")

if sexo == 'm':
    if estatura > 1.72:
        print("Usted es mas alto que la media de varones")
    else:
        print("Usted es igual o mas bajo que la media de varones")
else:
    if estatura > 1.65:
        print("Usted es mas alto que la media de mujeres")
    else:
        print("Usted es igual o mas bajo que la media de mujeres")
