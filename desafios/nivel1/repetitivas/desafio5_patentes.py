# DESAFÍO 5
# Se está desarrollando un sistema de control de vehículos desde donde se han tirado restos de basura a la vía pública.

# Para ello la ciudad cuenta con sistemas de monitoreo de patentes que devuelve 3 letras y un valor numérico de 5 dígitos 
# a la Central con el siguiente significado:

# 3 letras: Correspondientes a la patente.

# Del valor numérico:

# Los 3 primeros números corresponden a la patente

# El 4 número indica

# 1- Tiró basura a la vía pública

# 0 - No tiró basura a la vía pública

# El 5 número indica

# 1- Ya había sido multado el vehículo

# 0 - Vehículo sin multas.

# Deberás informar cantidad de vehículos observados, cantidad de vehículos que han tirado basura y porcentaje de éstos que ya habían sido multados.


vehiculos = 0
tiraron_basura = 0
basura_multados = 0

print("Presione solo enter para terminar y proceder al análisis")
seguir = True
while seguir:
    cod_patente = input("Ingrese la patente (sin espacios): ")
    if cod_patente:
        vehiculos += 1
        tiro_basura = cod_patente[-2]
        multado = cod_patente[-1]
        if tiro_basura == "1":
            tiraron_basura += 1
            if multado == "1":
                basura_multados += 1
    else:
        seguir = False

print()
print("Total vehículos: ", vehiculos)
print("Total tiraron basura:", tiraron_basura)
print("Porcentaje de reincidentes sobre primera falta:",
      basura_multados*100/tiraron_basura if tiraron_basura else "No aplica")
