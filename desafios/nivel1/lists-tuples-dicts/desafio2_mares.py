# Desafío 2 #
# Crea una tupla con los factores que más afectan a los mares.
# Luego para jugar con niñoy y niñas, aperndiendo sobre
# contaminación del agua crea un programa que pida números,
# si el número está entre 1 y la longitud máxima de la tupla,
# muestra el contenido en esa posición sino muestra un mensaje de error.
# El programa termina cuando el usuario introduce un cero.


factores = (
    "Aguas residuales", "sustancias químicas tóxicas", "aguas pluviales", "vertido de plásticos",
    "vertidos de petróleo", "actividad minera en alta mar", "cambio climático",
)

print("Aprenda sobre los factores que afectan a los mares...")
while True:
    ingreso = input("Ingrese un número (del 1 al 7) o '0' para salir: ")
    if ingreso:
        if ingreso.isdigit():
            ingreso = int(ingreso)
            if ingreso in range(1, len(factores) + 1):
                ingreso -= 1
                print(f"Bingo: el factor correspondiente al {ingreso} es:", factores[ingreso].title())
            elif ingreso == 0:
                print("Saliendo...")
                break
            else:
                print(f"AVISO: Ingrese solos números del 1 al {len(factores)}, o '0' para salir")
        else:
            print("AVISO: Ingrese solo números")
    else:
        print("AVISO: Ingrese solo números")

