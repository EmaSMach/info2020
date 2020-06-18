# DESAFÍO 3
# En una tienda de descuento por reciclado las personas que van a pagar el importe de su compra 
# llegan a la caja y ofrecen tapitas para reciclar, de acuerdo a la cantidad que lleven en la 
# caja le entregan un código de descuento que se aplicará sobre el total de su compra. 
# Determinar la cantidad que pagara cada cliente desde que la tienda abre hasta que cierra. 

# Se sabe que si el código de descuento es rojo se obtendrá un 40% de descuento; 
# si es amarilla un 25% y si es blanca no obtendrá descuento.


seguir = True
while seguir:
    answer = input("Ingresar cliente s/n?: ").lower()
    if answer != "s":
        seguir = False
    else:
        print("Presione enter para terminar de ingresar productos")
        otro_producto = True
        total = 0
        while otro_producto:
            importe_producto = input("Importe producto: ")
            if importe_producto:
                if importe_producto.isdigit():
                    total += int(importe_producto)
                else:
                    otro_producto = False
            else:
                otro_producto = False
        valid = False
        descuento = 0
        while not valid:
            print("""
            Elija color de código de descuento:
            1) Blanco
            2) Amarillo
            3) Rojo
            """)
            color = input("Respuesta: ")
            if color.isdigit():
                color = int(color)
                if color == 1:
                    descuento = 0
                    valid = True
                elif color == 2:
                    descuento = 25
                    valid = True
                elif color == 3:
                    descuento = 40
                    valid = True
                else:
                    print("\nOpción inválida\n")
            else:
                print("\nOpción inválida\n")

        print("Total: ", total)
        print("Despuento: ", descuento, "%")
        print("Totoal a pagar: ", total - (descuento*total/100))
