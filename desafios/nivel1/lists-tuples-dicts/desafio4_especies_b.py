# Desafio 4
# escribir un programa que cargue una tupla con nombres de especie, y para cada nombre de especie imprima el mensaje
# 'Hola soy ....., cuidame'.
# Modificá el programa anterior y dada una posición inicial 'p' y una cantidad 'n'
# imprima el mensaje anterior para los n nombres que se encuentrarn a partir de la posición 'i'.


especies = (
    'perro', 'gato', 'mandioca', 'remolacha', 'tigre', 'jirafa', 'zapallo', 'rúcula', 'uva',
    'león', 'gallina', 'álamo', 'topo', 'camaleón',
)

while True:
    p = int(input("Ingrese la posición inicial desde donde imprimir el saludo: "))
    if p in range(len(especies)):
        pass
    else:
        print("Posición no válida, intente nuevamente")
        continue
    n = int(input("Ingrese la cantidad de animales que saludarán: "))
    if n:
        especies = especies[p-1:]
        print()
        for i in range(n):
            print(f"Hola, soy {especies[i]}, cuidame.")
    break
