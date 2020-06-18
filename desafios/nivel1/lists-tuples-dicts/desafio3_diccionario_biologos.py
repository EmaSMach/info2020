# Desafío 3
# Crea un diccionario donde la
# clave sea el nombre de biólogos
# y el valor sea el email (no es necesario validar).
# Tendrás que ir pidiendo contactos hasta el usuario
# diga que no quiere inseertar mas. No se podrán inertar
# nombres repetidos.
from pprint import pprint


contactos = {}

while True:
    answer = input("Ingresar contacto (s/n)?: ")
    if answer in 'snSN':
        if answer in 'sS':
            while True:
                nombre = input("Nombre: ").lower()
                # verificamos que no estemos intetando ingresar un contacto ya existente
                if nombre:
                    if nombre not in contactos:
                        break
                    else:
                        print("El contacto ya existe, ingrese otro")
                        continue
                else:
                    print("Debe ingresar un nombre")
            while True:
                email = input("E-mail: ").lower()
                if email:
                    break
                else:
                    print("Debe ingresar un email")
            # verificamos que se hayan ingresado valores en ambos campos
            contactos[nombre] = email
            print("Contacto agregado", nombre, email)
        else:
            print("Saliendo...")
            break
    else:
        print("AVISO: Respuesta no válida, intente nuevamente")

if contactos:
    for contacto in contactos.items():
        print("Nombre:", contacto[0], "Email:", contacto[1])
else:
    print("No se han ingresado contactos")
