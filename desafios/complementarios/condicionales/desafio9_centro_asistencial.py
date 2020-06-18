# # Desafío 9
# En un Centro Asistencial existen tres áreas: Pediatría, Traumatología y Kinesiología. 
# El presupuesto anual del hospital se reparte conforme a la sig. tabla:

# ÁREA 		        PORCENTAJE

# Pediatría			60%

# Traumatología		20%

# Kinesiología		20%


# Obtener la cantidad de dinero que recibirá cada área, para cualquier monto presupuestal que se ingrese por teclado.

PEDIATRIA = 60
TRAUMATOLOGIA = 20
KINESIOLOGIA = 20

presupuesto = int(input("Presupuesto: "))

print(f"Al área de Pediatría le corresponde el {PEDIATRIA}%: $ {presupuesto*PEDIATRIA/100}")
print(f"Al área de Traumatología le corresponde el {TRAUMATOLOGIA}%: $ {presupuesto*TRAUMATOLOGIA/100}")
print(f"Al área de Kinesiología le corresponde el {KINESIOLOGIA}%: $ {presupuesto*KINESIOLOGIA/100}")
