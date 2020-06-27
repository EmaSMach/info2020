# Mostrar los perímetros de varios triángulos ingresados sus lados por teclado, hasta que ya no desee.


otro = True
while otro:
    lado1 = float(input("Lado 1: "))
    lado2 = float(input("Lado 2: "))
    lado3 = float(input("Lado 3: "))
    print(f"El perímetro del {lado1 + lado2 + lado3}")
    
    while True:
        continuar = input("Continuar? (s/n): ")
        if continuar and continuar in 'sn':
            if continuar == 's':
                break
            else:
                otro = False
                break
        else:
            print("Error, intente otra vez")
