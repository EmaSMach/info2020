# DESAFÍO 1
# Nos han pedido desarrollar una aplicación móvil para reducir comportamientos inadecuados para el ambiente.

# a) Te toca escribir un programa que simule el proceso de Login. Para ello el programa debe preguntar 
# al usuario la contraseña, y no le permita continuar hasta que la haya ingresado correctamente.

# b) Modificar el programa anterior para que solamente permita una cantidad fija de intentos. 


"""version without a break statement"""
intentos = 2
flag = False
while intentos != 0 and flag is False:
    usuario = input("Usuario: ")
    password = input("Contraseña: ")
    intentos -= 1
    if usuario == "User1" and password == "Correct":
        print("\n***Bienvenido a la app que cuida el medio ambiente***")
        flag = True
        # break
    else:
        if intentos:
            print("\nDatos Incorrectos, inténtelo nuevamente, intentos restantes", intentos, "\n")
        else:
            print("\nSaliendo...")
