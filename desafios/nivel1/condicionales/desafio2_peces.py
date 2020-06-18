# La contaminación del agua se detecta en los laboratorios,  
# donde pequeñas muestras de agua se analizan para diversos tipos de contaminantes. 
# Los organismos vivos tales como pescados se pueden también utilizar para la detección de la contaminación del agua.
# Los cambios en su comportamiento o crecimiento nos demuestran,  que el agua en la que viven está contaminada.

# Para seguir colaborando en esta misión de salvar al planeta, necesitamos que elabores un programa en Python que
#  dado el tamaño de un pez indique si su organismo está contaminado. Para ello tendremos 4 opciones:

# Tamaño Normal: Mensaje "Pez en buenas condiciones"

# Tamaño por debajo de lo Normal: Mensaje "Pez con problemas de nutrición"

# Tamaño un poco por encima de lo Normal: Mensaje "Pez con síntomas de organismo contaminado"

# Tamaño sobredimensionado: Mensaje "Pez contaminado"


def menu_opciones():
    """Muestra un menú, y devuelve la opción elegida por el usuario"""
    print("""
    1) Tamaño Normal
    2) Tamaño por debajo del Normal
    3) Tamaño por un poco por encima del Normal
    4) Tamaño sobredimensionado
    """)
    return int(input("Elija la opción correspondiente al tamaño del pez: "))


respuesta = menu_opciones()

print() # esto solo agrega una línea vacía
if respuesta == 1:
    print("Pez en buenas condiciones")
elif respuesta == 2:
    print("Pez con problemas de nutrición")
elif respuesta == 3:
    print("Pez con síntomas de organismo contaminado")
elif respuesta == 4:
    print("Pez contaminado")
