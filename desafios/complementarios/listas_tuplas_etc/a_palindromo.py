# Ingresar una palabra, carácter por carácter, en una lista y determinar si es palíndromo.


palabra = "añá"
palabra = [letra for letra in palabra]


def clean(lista: list):
    """Limipia la lista de letras de las tildes y diéresis"""
    vocales = {
        'á': 'a',
        'é': 'e',
        'í': 'i',
        'ó': 'o',
        'ú': 'u',
        'ü': 'u'
    }
    for vocal in vocales:
        if vocal in lista:
            lista[lista.index(vocal)] = vocales.get(vocal)
    return lista


def es_palindromo(lista: list):
    """Determina si la palabra pasada en forma de lista de letras es palíndromo"""
    lista = clean(lista)
    return lista == lista[::-1]


print("Es palíndromo: ", es_palindromo(palabra))
