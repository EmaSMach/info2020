# # Desafío 6
# Un equipo de fútbol ha tenido una buena campaña y desea premiar a sus jugadores 
# con un aumento del salario para la siguiente campaña. 
# Los sueldos deben ajustarse de la siguiente forma:

# Sueldo Actual (en $)            Aumento

# 0 – 6000						15%

# 6000 – 7900					    10%

# 7900 – 12000					6%

# Más de 12000				    0%

# Diseñar un programa que lea el salario de un jugador, y que a continuación 
# muestre el tanto por ciento de aumento, el sueldo actual y el sueldo aumentado.


sueldo = int(input("Sueldo: "))
aumento = 15 if sueldo >= 0 and sueldo <= 6000 else \
          10 if sueldo >= 6001 and sueldo <= 7900 else \
          6 if sueldo >= 7901 and sueldo <= 12000 else 0


print(f"Le corresponde un aumento del {aumento}, sueldo actual $ {sueldo}, sueldo aumentado $ {sueldo + (sueldo*aumento/100)}")
