# Desafío 19
# Una distribuidora de libros vende a librerías y a particulares. Aplica bonificaciones por cantidad según el siguiente criterio:

# i.      a librerías: hasta 24 unidades, el 20%; más de 24 unidades, el 25%.

# ii.      a particulares: menos de 6 unidades, nada; desde 6 hasta 18 unidades, el 5% y más de 18 unidades, el 10%.

# El tipo de cliente está codificado así: 'L' para librerías, 'P' para particular. 
# Dado el importe bruto de una compra de libros, el tipo de cliente de que se trata y la cantidad total pedida por el mismo, 
# determinar el importe bruto bonificado.


while True:
    tipo_cliente = input("""Tipo Cliente (L)-Librería / (P)-Particular: """).upper()
    if tipo_cliente and tipo_cliente in "PL":
        break
    else:
        print("No válido, ingrese L prar Librería o P para Particular")

cantidad_libros = int(input("Cantidad de libros: "))
importe_bruto = float(input("Importe bruto: $ "))

if tipo_cliente == 'P':
    if cantidad_libros < 6:
        descuento = 0
    elif 6 <= cantidad_libros <= 18:
        descuento = 5
    else:
        descuento = 10
else:
    if cantidad_libros <= 24:
        descuento = 20
    else:
        descuento = 25

print()
print("Gracias por su compra")
print(f"Tipo cliente: {'Particular' if tipo_cliente == 'P' else 'Librería'}")
print(f"Unidades compradas: {cantidad_libros}")
print(f"Porcentaje Descontado: {descuento} %")
print(f"Subtotal sin descuento: {importe_bruto}")
print(f"Total descontado: $ {importe_bruto*descuento/100}")
print(f"Total a pagar: $ {importe_bruto - (importe_bruto*descuento/100)}")
