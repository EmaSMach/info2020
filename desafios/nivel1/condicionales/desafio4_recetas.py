# DESAFÍO 4
# Tenemos que decidir entre 2 recetas ecológicas. Los ingredientes para cada tipo de receta aparecen a continuación.

# Ingredientes comunes: Verduras y berenjena.

# Ingredientes Receta 1: Lentejas y apio.

# Ingredientes Receta 2: Morrón y Cebolla..

# Escribir un programa que pregunte al usuario que tipo de receta desea, y en función de su respuesta 
# le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir 3 ingrediente 
# (entre la receta elegida y los comunes.) y el tipo de receta. Al final se debe mostrar por pantalla 
# la receta elegida y todos los ingredientes.


print("Elija se receta:\n"
      "\t1) Receta 1\n"
      "\t2) Receta 2\n")

receta_elegida = int(input("Respuesta: "))

if receta_elegida == 1:
    print("Elija el ingrediente:\n"
          "\t1) Lentejas\n"
          "\t2) Apio\n")
    ingrediente_elegido = int(input("Respuesta: "))
else:
    print("Elija el ingrediente que desea:\n"
          "\t1) Morrón\n"
          "\t2) Cebolla\n")
    ingrediente_elegido = int(input("Respuesta: "))

if receta_elegida == 1:
    ingrediente = "Lentejas" if ingrediente_elegido == 1 else "Apio"
else:
    ingrediente = "Morrón" if ingrediente_elegido == 1 else "Cebolla"

print(f"\nUsted elijió la receta {receta_elegida} con los siguientes ingredientes:")
print("Verduras")
print("Berenjenas")
print(f"{ingrediente}")
