# # Desafío 13
# En un supermercado se hace una promoción, mediante la cual el cliente obtiene un 
# descuento dependiendo de un número que se escoge al azar. Si el numero escogido es 
# menor que 74 el descuento es del 15% sobre el total de la compra, si es mayor o 
# igual a 74 el descuento es del 20%. Obtener cuánto dinero se le descuenta.


numero = int(input("Número: "))
if numero < 74:
    descuento = 15
else:
    descuento = 20

compra = int(input("Total Compra: "))
print(f"Compra: $ {compra}")
print(f"Porcentaje descontado: {descuento} %")
print(f"Monto descontado: $ {compra*descuento/100}")
print(f"Total a pagar12 $ {compra - (descuento*compra/100)}")
