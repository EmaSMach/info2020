# DESAFÍO 5
# La ciudad esta dividida en 2 secciones de recolección sección A y B de acuerdo al nombre de la 
# barrio y el tipo del barrio (CÉNTRICO y NO CÉNTRICO)

# La sección A esta formada por los barrios céntricos cuyo nombre comienza con 
# una letra anterior a M y los barrios no céntricos con nombre posterior a la M, y la sección B el resto.

# Debemos hacer un programa que dado el nombre del barrio y la ubicación, nos informe en que sección se encuentra.


from string import ascii_lowercase # esto es una lista de letras


letras = list(ascii_lowercase)
# acá inserto la ñ en la lista de letras
letras.insert(letras.index("n") + 1, "ñ")

# pido el nombre del barrio
nombre_barrio = input("Ingrese el nombre del barrio: ").lower()
print("""Ingrese la ubicación de su barrio:
    1) Céntrico
    2) No céntrico
""")

ubicacion_barrio = input("Respuesta: ") # acá ingresa 1 o 2

# empiezo a comparar
# si primera letra del barrio     es menor a la m      y  es céntrico           o
if letras.index(nombre_barrio[0]) < letras.index("m") and ubicacion_barrio == "1" or \
   letras.index(nombre_barrio[0]) > letras.index("m") and ubicacion_barrio == "2":
   # si la primera letra del barrio es mayor a la m    y  no es céntrico
   # -----------------------
   # la seccion del barrio es A
    seccion = "A"
else:
    # si no la sección es B
    seccion = "B"

print()
print(f"La sección del barrio ingresado es: {seccion}")
