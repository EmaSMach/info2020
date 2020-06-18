# Desafío 3
# Para el uso de fertilizantes es necesario medir cuánto abarca un determinado compuesto en el suelo 
# el cual debe existir en una cantidad de al menos 10% por hectárea, y no debe existir vegetación del tipo MATORRAL. 
# Escribir un programa que determine si es factible la utilización de fertilizantes.


def usar_fertilizantes(parte_por_millon, tipo_maleza):
    if parte_por_millon >= 10 and tipo_maleza.lower() != 'maleza':
        return True
    else:
        return False


compuesto = int(input("Ingrese partes por millón del compuesto: "))
tipo_de_maleza = input("Ingrese el tipo de maleza: ")

if usar_fertilizantes(compuesto, tipo_de_maleza):
    print("Se puede usar fertilizantes en este terreno")
else:
    print("No se puede usar fertilizantes en este suelo")
