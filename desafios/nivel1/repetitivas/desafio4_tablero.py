# DESAFÍO 4
# Escriba un programa que permita imprimir un tablero Ecológico (verde y blanco) de acuerdo al tamaño indicado. 
# Por ejemplo el gráfico a la izquierda es el resultado de un tamaño: 8x6


print("Ingrese tamaño del tablero")
alto = input("Alto: ")
ancho = input("Ancho: ")
print()
if alto.isdigit() and ancho.isdigit():
    ancho = int(ancho)
    alto = int(alto)
    color = "Verde"
    for fila in range(alto):
        first = color  # Keep the color of the first square
        for columna in range(ancho):
            print(color, " ", end='')  # Should print on the same line
            # Switching colors
            color = "Blanco" if color == "Verde" else "Verde"
        # setting the color according to the previous first square
        color = "Blanco" if first == "Verde" else "Verde"
        print()  # linebreak
