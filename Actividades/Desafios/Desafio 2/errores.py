import estilo as e
class ErrorAsiento(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)
    
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

#validar strings
def validar_str(cadena):
    while True:
        try:
            entrada = input(e.datos(cadena))
            
            for caracter in entrada:
                if caracter.isdigit():
                    raise ValueError
            
            break
        
        except ValueError:
            print(e.error("Error, la entrada no puede contener numeros"))
    
    return entrada

def validar_vuelo(vuelos, cadena, tipo): #para no repetir codigo, el tipo lo utilizo para validar vuelos pero en dos ocaciones distintas (me cambia el parametro vuelos) 
    while True:
        try: 
            if tipo==1:
                c=0
                entrada = int(input(e.datos(cadena)))
                for vuelo in vuelos:
                    if vuelo[0]==entrada:
                        c+=1
                    
                if c==0: #el numero de vuelo no existe
                        raise TypeError
            else:
                c=0
                entrada = int(input(e.datos(cadena)))
                for vuelo in vuelos:
                    if vuelo[0][0]==entrada:
                        c+=1
                    
                if c==0: #el numero de vuelo no existe
                        raise TypeError
                
            break
        except ValueError:
            print(e.error("Error, se esperaba un numero como entrada"))
        
        except TypeError:
            print(e.error("El vuelo ingresado no existe"))
    
    return entrada
            
        