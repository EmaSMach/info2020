# Leer una frase y luego invierta el orden de las palabras en la frase.
# Por Ejemplo: “una imagen vale por mil palabras” debe convertirse en “palabras mil por vale imagen una”.


def invertir_frase(frase):
    frase = frase.split()
    return " ".join(frase[::-1])


print(invertir_frase("una imagen vale por mil palabras"))
