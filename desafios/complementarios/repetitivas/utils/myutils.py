def continuar(mensaje='Desea continuar? (s/n): '):
    while True:
        answer = input(mensaje)
        if answer and answer in 'sn':
            if answer == 's':
                return True
            else:
                return False
        else:
            print("Intente otra vez")

# continuar()
