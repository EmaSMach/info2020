# Desafío 16
# Hacer un programa que calcule el total a pagar por la compra de camisas. 
# Si se compran tres camisas o mas se aplica un descuento del 20% sobre el 
# total de la compra y si son menos de tres camisas un descuento del 10%.


cantidad_camnisas = int(input("Camisas Compradas: "))
precio_camisa = float(input("Precio camisa: "))

if cantidad_camnisas >= 3:
    descuento = 20
else:
    descuento = 10

subtotal = precio_camisa * cantidad_camnisas

print(f"Total a pagar: $ {subtotal - (subtotal*descuento/100)}")
