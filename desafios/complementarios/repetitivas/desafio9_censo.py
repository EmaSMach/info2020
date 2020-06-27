# Desafío 9
# Un censador recopila ciertos datos aplicando encuestas para 
# el último Censo Nacional de Población y Vivienda. 
# Desea obtener de todas las personas que alcance a encuestar en un día, 
# que porcentaje tiene estudios de primaria, secundaria, carrera técnica, 
# estudios profesionales y estudios de posgrado.


personas = {}
id_ = 1
continuar = True
while continuar:
    persona = input("Nombre: ")
    if persona:
        personas[id_] = {'nombre': persona}
    while True:
        menu_estudios = """Elija el nivel de estudios
        1) Primaria
        2) Secundaria
        3) Carrera Técnica
        4) Estudios Profesionales
        5) Estudios de Posgrado
        """
        print(menu_estudios)
        eleccion = input("Respuesta: ")
        if eleccion and eleccion in "12345":
            personas[id_]['estudios'] = eleccion
            break
        else:
            print("Error, intente otra vez")
    id_ += 1
    while True:
        answer = input("Ingresar otra persona? (s/n): ")
        if answer and answer in 'sn':
            if answer == 's':
                break
            else:
                continuar = False
                break
        else:
            print("Error, intente otra vez")

print(personas)
primarias = 0
secundarias = 0
terciarias = 0
profesionales = 0
universitarios = 0
for person in personas.values():
    if person['estudios'] == '1':
        primarias += 1
    elif person['estudios'] == '2':
        secundarias += 1
    elif person['estudios'] == '3':
        terciarias += 1
    elif person['estudios'] == '4':
        profesionales += 1
    elif person['estudios'] == '5':
        universitarios += 1

total_personas = len(personas)
print("Total: ", total_personas, "personas")
print(f"Estudios Primarios: {primarias} personas , {100*primarias/total_personas} %")
print(f"Estudios Secundarios: {secundarias} personas , {100*secundarias/total_personas} %")
print(f"Estudios Terciarios: {terciarias} personas , {100*terciarias/total_personas} %")
print(f"Estudios Profesionales: {profesionales} personas , {100*profesionales/total_personas} %")
print(f"Estudios Universitarios: {universitarios} personas , {100*universitarios/total_personas} %")
