# Desafío 1
# 150 años es el tiempo que tarda una bolsa de plástico común en degradarse y una botella de PET puede tardar 1.000 años en desaparecer. 

# Por otro lado los Envases de tetrabrik pueden tardar hasta 30 años en degradarse.

# Un trozo de chicle tarda 5 años en degradarse. 

# Se solicita una función para que dado el ingreso de un elemento, 
# se solicite tipo: Bolsa de plástico, botella PET, envase tetrabrik o chicle, 
# e imprima la cantidad de años que tarda en degradarse.


def calcular_degradacion(tipo):
    elements = {
        1: (150, "Bolsa de Plástico",),
        2: (1000, "Botella de PET",),
        3: (30, "Envase de Tetrabrick",),
        4: (5, "Chicle"),
    }
    return elements[tipo]


def menu_tipo():
    while True:
        print(""" Elija el tipo de elemento:
        1) Bolsa de Plástico común
        2) Botella de PET
        3) Envase Tetrabrick
        4) Chicle
        """)
        eleccion = input("Respuesta: ")
        if eleccion:
            if eleccion.isdigit():
                eleccion = int(eleccion)
                if eleccion in (1, 2, 3, 4,):
                    return eleccion
                else:
                    print("Solo número del 1 al 4")
            else:
                print("Ingrese solo números")
        else:
            print("No válido, intente otra vez")


def calcular():
    # creo que elemento puede omitirse, no es necesario
    elemento = input("Ingrese el elemento: ")
    tipo = menu_tipo()
    anios, tipo_elemento = calcular_degradacion(tipo)
    print(f"El {elemento} de tipo {tipo_elemento} tarda {anios} años en degradarse")


calcular()
