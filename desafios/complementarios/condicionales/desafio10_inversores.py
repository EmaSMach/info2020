# Desafio 10
# Tres personas deciden invertir su dinero para fundar una empresa. 
# Cada una de ellas invierte una cantidad distinta. 
# Obtener el porcentaje que cada quien invierte con respecto a la cantidad total invertida.


persona1 = float(input("Inversión persona 1: "))
persona2 = float(input("Inversión persona 2: "))
persona3 = float(input("Inversión persona 3: "))

total = persona1 + persona2 + persona3

print(f"La primera persona invirtió el {100*persona1/total} % de los $ {total}")
print(f"La segunda persona invirtió el {100*persona2/total} % de los $ {total}")
print(f"La tercera persona invirtió el {100*persona3/total} % de los $ {total}")
