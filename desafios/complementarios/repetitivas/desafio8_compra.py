# Desafiío 8
# Diseñar un programa que permita calcular el total de una compra, ingresando cantidad y precio de los productos. 
# El programa debe estar preparado para que el ingreso de los datos se produzca hasta que el usuario lo desee.


total = 0
while True:
    answer = input("\nDesea ingresar un producto? (s/n): ")
    if answer in 'sn':
        if answer == 'n':
            break
        else:
            precio_unitario = input("Precio Unitario: ")
            if precio_unitario.isdecimal():
                precio_unitario = float(precio_unitario)
            else:
                print("No válido, intente otra vez")
            cantidad = input("Cantidad: ")
            if cantidad.isdigit():
                cantidad = int(cantidad)
                if cantidad > 0:
                    pass
                else:
                    print("La cantidad mínima es 1")
            else:
                print("No válido, intente otra vez")

            total += precio_unitario * cantidad
    else:
        print("Respuesta inválida, intente otra vez")

print(f"\nEl total a pagar es: $ {total}")