# Desafío 5
# Diseñar un programa que lea las longitudes de los tres lados de un triángulo (L1,L2,L3) 
# y determine qué tipo de triángulo es, de acuerdo a los siguientes casos. 
# Suponiendo que A determina el mayor de los tres lados y B y C corresponden con los otros dos, entonces:

# Si A>=B + C à No se trata de un triángulo

# Si A2 = B2 + C2 à Es un triángulo rectángulo

# Si A2 > B2 + C2 à Es un triángulo obtusángulo

# Si A2 < B2 + C2 à Es un triángulo acutángulo

# num1 if (mayor == num2 and menor == num3) or (mayor == num3 and menor == num2) else \
#         num2 if (mayor == num1 and menor == num3) or (mayor == num3 and menor == num1) else num3


l1 = float(input("Lado 1: "))
l2 = float(input("Lado 2: "))
l3 = float(input("Lado 3: "))
a = l1 if l1 > l2 and l1 > l3 else (l2 if l2 >  l3 else l3)
c = l1 if l1 < l2 and l1 < l3 else (l2 if l2 <  l3 else l3)
b = l1 if (a == l2 and c == l3) or (a == l3 and c == l2) else \
    l2 if (a == l1 and c == l3) or (a == l3 and c == l1) else l3

print(a, b, c)

if a >= (b + c):
    print("No es un triángulo")
elif a**2 == (b**2 + c**2):
    print("Triángulo RECTÁNGULO")
elif a**2 > (b**2 + c**2):
    print("Triángulo OBTUSÁNGULO")
elif a**2 < (b**2 + c**2):
    print("Triángulo ACUTÁNGULO")
