# Calcular el monto a pagar por cada cliente y total recaudado en una estación de servicio. 
# Debe diseñar un programa que permita monto por cliente y el total recaudado por la gasolinera, 
# tomando en cuenta lo siguiente:

# • El precio del litro es para el Tipo A $50, para el Tipo B $ 55 y para el Tipo C $60

# • El programa finaliza cuando se introduce una D como tipo de gasolina.
from utils.myutils import continuar


precio_a = 50
precio_b = 55
precio_c = 60


while True:
    tipo = input("""********************************
    Ingrese Tipo [A, B, C]
    Ingrese <D> para salir

    Respuesta: """).lower()
    if tipo and tipo in 'abcd':
        if tipo == 'd':
            break
        elif tipo == 'a':
            litros = float(input("Litros: "))
            print(f"El monto a pagar es {litros*precio_a}")
        elif tipo == 'b':
            litros = float(input("Litros: "))
            print(f"El monto a pagar es {litros*precio_b}")
        else:
            litros = float(input("Litros: "))
            print(f"El monto a pagar es {litros*precio_c}")
    else:
        print("Respuesta inválida, intente otra vez")

