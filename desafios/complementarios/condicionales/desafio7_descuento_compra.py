# Desafio 7
# Un comercio ofrece un descuento del 15% sobre el total de la compra si esta supera los $1000. 
# Obtenga para determinado cliente cuánto deberá pagar finalmente por su compra 
# y el descuento obtenido, si es que corresponde.


compra = float(input("Monto compra: "))
descuento = 15 if compra > 1000 else 0

print(f"Ustede debe pagar {compra - (compra*descuento/100)}, su descuento es del {descuento}% = {compra*descuento/100}")
