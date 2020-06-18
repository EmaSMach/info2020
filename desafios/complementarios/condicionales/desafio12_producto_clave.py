# Desafío 12
# Hacer un programa que imprima el nombre de un artículo, clave, 
# precio original y su precio con descuento. El descuento lo hace en base a la clave, 
# si la clave es 01 el descuento es del 10% y si la clave es 02 el descuento en del 20% 
# (solo existen dos claves).


producto = input("Producto: ")
while True:
    clave = input("Clave: ")
    if clave == "01":
        descuento = 10
        break
    elif clave == "02":
        descuento = 20
        break
    else:
        print("Clave errónea, intente de nuevo")

precio = float(input("Precio: "))

print()
print(f"Nombre:                 {producto}")
print(f"Clave:                  {clave}")
print(f"Nombre:                 {descuento}")
print(f"Precio original:        {precio}")
print(f"Precio con decuento:    {precio-(precio*descuento/100)}")
