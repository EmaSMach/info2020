import os
import random


palabras = ['hola', 'mundo', 'camino', 'delgado', 'implementación', 'modelo', 'entidad',
            'relación', 'certeza', 'arreglo', 'sincero', 'animal', 'luciérnaga', 'cigüeña']



def mostrar_gente(errores):
    """Va armando el muñeco de acuerdo a la cantidad de errores que le pasemos, y lo muestra."""
    if errores > 7:
        raise ValueError("'errores' debe ser de 0 a 7")
    partes = ['O', '|', '\\', '/', '|', '/', '\\']
    p = [elem[1]  if elem[0] < errores else ' ' for elem in enumerate(partes)]
    gente = f"""
    ______
    |  	 {p[0]}
    |  	{p[2]}{p[1]}{p[3]}
    |  	 {p[4]}
    |   {p[5]} {p[6]}
    |

    """
    print(gente)


def banner_ahorcado():
    print(
    """
    ###################
    #    AHORCADO     #
    ###################
    """
    )


def menu_inicio():
    menu_string = """
    ###########
    1- Jugar
    2- Salir
    ###########

    """
    while True:
        os.system("cls")
        print(menu_string)
        respuesta = input("Respuesta: ")
        if respuesta and respuesta in '12':
            if respuesta == '1':
                return True
            else:
                return False
        else:
            print("Intente otra vez")


def elegir_palabra(lista_palabras):
    return random.choice(lista_palabras)


def letra_ya_ingresada(letra, letras_ingresadas):
    if letra in letras_ingresadas:
        return True
    else:
        return False


def pedir_letra2():
    while True:
        letra = input("Letra: ")
        if letra.isalpha() and len(letra) == 1:
            return letra.lower()
        else:
            print("Error, ingrese una letra")


def pedir_letra():
    letra = input("Letra: ")
    if letra.isalpha() and len(letra) == 1:
        return letra.lower()
    else:
        return False


vocales = {
    'á': 'a',
    'é': 'e',
    'í': 'i',
    'ó': 'o',
    'ú': 'u',
    'ü': 'u',
}

def jugar():
    mensaje = ""
    letras_ingresadas = []
    palabra = elegir_palabra(palabras)
    # quitamos los acentos, diéresis
    fixed_palabra = [vocales[l] if l in vocales else l for l in palabra]
    placeholders =  ['_' for letra in palabra]
    vivo = True
    errores = 0
    while True:
        os.system('cls')
        banner_ahorcado()
        print()
        print(' '*4, ' '.join(p.upper() for p in placeholders))
        print()
        mostrar_gente(errores)
        if not vivo:
            print("PERDISTE!!")
            print(f"Palabra: {palabra}")
            return
        # chequeamos si ganó comparando lo que ya ingresó
        # con la palabra elegida por el sistema
        if ''.join(placeholders) == palabra:
            print("GANASTE")
            break
        print(mensaje)
        mensaje = ""
        letra = pedir_letra()
        if not letra:
            mensaje = "Ingrese solo una letra"
            continue
        if letra_ya_ingresada(letra, letras_ingresadas):
            mensaje = "Letra ya ingresada, intente otra vez"
            continue
        # Si la letra está en la palabra (sin tener en cuenta tildes)
        if letra in fixed_palabra:
            for pos, fixed_letra in enumerate(fixed_palabra):
                if letra == fixed_letra:
                    placeholders[pos] = palabra[pos]
        else:
            errores += 1
            if errores == 7:
                vivo = False
        letras_ingresadas.append(letra)


def main():
    continuar = menu_inicio()
    if continuar:
        jugar()
    else:
        return


if __name__ == '__main__':
    main()
