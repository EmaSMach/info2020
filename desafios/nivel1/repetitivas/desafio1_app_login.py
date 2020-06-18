# DESAFÍO 1
# Nos han pedido desarrollar una aplicación móvil para reducir comportamientos inadecuados para el ambiente.

# a) Te toca escribir un programa que simule el proceso de Login. Para ello el programa debe preguntar 
# al usuario la contraseña, y no le permita continuar hasta que la haya ingresado correctamente.

# b) Modificar el programa anterior para que solamente permita una cantidad fija de intentos. 


while True:
    usuario = input("Usuario: ")
    password = input("Contraseña: ")
    if usuario == "User1" and password == "Correct":
        print("\n***Bienvenido a la app que cuida el medio ambiente***")
        break
    print("\nDatos Incorrectos, inténtelo nuevamente\n")
