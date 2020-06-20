# Desafío 15
# Un obrero necesita calcular su salario semanal, el cual se obtiene de la siguiente manera:

# i. Si trabaja 40 horas o menos se le paga $16 por hora
# ii. Si trabaja más de 40 horas se le paga $16 por cada una de las primeras 40 horas y $20 por cada hora extra.


horas_trabajadas = int(input("Horas: "))
if horas_trabajadas <= 40:
    total_a_cobrar = horas_trabajadas * 16
else:
    horas_extra = horas_trabajadas - 40
    total_a_cobrar = (40 * 16) + (horas_extra * 20)

print(f"Total a cobrar: {total_a_cobrar}")
