# Elabore un programa que dada una lista de 15 elementos, 
# copie en otra lista los elementos pares multiplicados por 2.

def copiar_elementos_pares(lista_origen, lista_destino):
    """Copia elementos en POSICIONES pares en otra lista, multiplicados por 2"""
    for pos, elemento in enumerate(lista_origen):
        if pos % 2 != 0:
            lista_destino.append(elemento*2)


origen = [1, 2, 3, 4, 5, 6]
destino = []

copiar_elementos_pares(origen, destino)
print(destino)
