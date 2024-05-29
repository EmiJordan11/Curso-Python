import estilo as e
    
#METODOS DE VALIDACION

#valida las opciones numericas
def validar_opcion(rango):
    while True:
        try:
            opcion = int(input(e.datos('Seleccione una opcion:')))
            if opcion<1 or opcion>rango:
                raise ValueError
            
            break
        except ValueError:
            print(e.error("Ingrese una opcion válida"))
    
    return opcion

#validar ints
def validar_int(cadena):
    while True:
        try:
            entrada = int(input(e.datos(cadena)))
            break
        except ValueError:
            print(e.error("Error, se esperaba un numero como entrada"))
            
    return entrada

        