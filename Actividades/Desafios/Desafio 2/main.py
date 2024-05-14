#IMPORTS
import random as r
import os
import estilo as e
import errores as err
import textwrap as tw

#GENERADORES
def generador_asientos(cantAsientos):
  asientos= [[r.randint(0,1) for x in range(4)] for y in range(cantAsientos//4)] #lo divido 10 ya que cada fila tiene 10 columnas
  return asientos

def contar_asientos_ocupados(matriz_asientos):
    total=0
    for fila in matriz_asientos:
        total+=sum(fila)
    return total
        

def generar_vuelos():
    vuelos=[]
    for x in range(10):
        #Generador de vuelos (numVuelo, origen, destino, fecha, matrizAsientos, asientosDisp, asientosTotales,precio)
        cantAsientos= r.choice(opcionesAsientos) #elijo cuantos asientos va a tener el vuelo
        matriz_asientos= generador_asientos(cantAsientos) #lleno asientos aleatoriamente
        
        #Genero el vuelo
        vuelos.append([r.randint (1000,2000),r.choice(paises), r.choice(paises), r.choice(fechas), matriz_asientos, cantAsientos - contar_asientos_ocupados(matriz_asientos), cantAsientos, r.randint(35000,80000)])
    return vuelos    

def generar_boleta(vuelo_elegido, asiento_elegido, n_tarjeta, nombre_tarjeta, dni_titular):
    return f'''**DETALLES DE LA COMPRA**
DETALLES DEL VUELO:
-Vuelo N°: {vuelo_elegido[0]}
-Origen: {vuelo_elegido[1]} 
-Destino: {vuelo_elegido[2]} 
-Fecha: {vuelo_elegido[3]}
                
DETALLES DEL ASIENTO:
-Fila: {asiento_elegido[0]}
-Columna: {asiento_elegido[1]}
                
DETALLES DEL PAGO:
-Numero de compra #{r.randint(20000,22000)}
-Precio total ${vuelo_elegido[7]}
-Numero tarjeta: {n_tarjeta}
-Nombre del titular: {nombre_tarjeta}
-DNI del titular: {dni_titular}
'''


#MODULOS
#mostrar menus
def mostrar_menus(num_menu):
    
    #Menu principal
    if num_menu==0:
        os.system('cls')
        
        print(e.titulo('BIENVENIDO!'))
        print(menu)
        
        opcion = err.validar_opcion(4)
            
        if opcion==1:
            buscar_vuelos()
        elif opcion==2:
            mostrar_vuelos()
        elif opcion==3:
            cancelar_reserva() 
        else:
            pass
    #Menu grilla asientos
    elif num_menu==1:
        print('\n'+e.subtitulo('DESEA VER LA GRILLA DE ASIENTOS DE UNO DE ESTOS VUELOS??'))
        print("1. Si\n2. No (volver al menu principal)")
        opcion= err.validar_opcion(2)
        
        if opcion==1:
            id_vuelo_elegido = err.validar_vuelo(vuelos, "Ingrese el numero de vuelo del que desea ver los asientos:",1)
            indice_vuelo_elegido = referenciar_vuelo(id_vuelo_elegido)
            os.system('cls')
            mostrar_asientos(vuelos[indice_vuelo_elegido])
            menu_comprar(vuelos[indice_vuelo_elegido])
        else: 
            mostrar_menus(0) 
            
    #Menu volver al principal
    else:
        print('\n'+e.subtitulo('DESEA REALIZAR OTRA CONSULTA?'))
        print("1. Si\n2. No")
        opcion= err.validar_opcion(2)
        if opcion==1:
            mostrar_menus(0)
            
        #else termina la ejecucion
            
            

def menu_comprar(vuelo_elegido):
    print('\n'+e.subtitulo('DESEA COMPRAR UN PASAJE PARA ESTE VUELO?'))
    print('1. Si\n2. No')
    
    opcion= err.validar_opcion(2)
    
    if opcion==1:
        comprar_pasajes(vuelo_elegido)
    else:
        mostrar_menus(0)

#referenciar vuelo
def referenciar_vuelo(id_vuelo): #tengo el id del vuelo pero no el indice que le corresponde en la lista VUELOS
    i=0
    for i, vuelo in enumerate(vuelos):
        if vuelo[0] == id_vuelo:
            return i #devuelvo el indice correspondiente en VUELOS
    
#Buscar vuelos filtrados
def buscar_vuelos():
    i=0 #para controlar cuantos vuelos muestro
    os.system('cls')
    print(e.titulo("SELECCIONE LOS FILTROS QUE DESEA UTILIZAR"))
    print("\n1. Buscar por Origen\n2. Buscar por Origen Y Destino\n3. Buscar por Origen, Destino y Fecha de vuelo")
    opcion= err.validar_opcion(3)
    
    print(e.subtitulo("\nIngrese los datos para filtrar los vuelos disponibles"))
    
    if opcion==1:
        origen = err.validar_str('Ingrese el origen del vuelo:')
        
        for vuelo in vuelos:
            if vuelo[1].lower()==origen.lower():
                print(e.azul('\nDATOS DEL VUELO:'))
                print(f'-Vuelo N°: {vuelo[0]}')
                print(f'-Origen: {vuelo[1]}')   
                print(f'-Destino: {vuelo[2]}') 
                print(f'-Fecha: {vuelo[3]}')      

                print('--------------------')
                i+=1 
                
    elif opcion==2:
        origen = err.validar_str('Ingrese el origen del vuelo:')
        destino = err.validar_str('Ingrese el destino del vuelo:')
        
        for vuelo in vuelos:
            if vuelo[1].lower()==origen.lower() and vuelo[2].lower()==destino.lower():
                print(e.azul('\nDATOS DEL VUELO:'))
                print(f'-Vuelo N°: {vuelo[0]}')
                print(f'-Origen: {vuelo[1]}')   
                print(f'-Destino: {vuelo[2]}') 
                print(f'-Fecha: {vuelo[3]}')      

                print('--------------------')
                i+=1
        
    else:
        origen = err.validar_str('Ingrese el origen del vuelo:')
        destino = err.validar_str('Ingrese el destino del vuelo:')
        fecha = err.validar_str('Ingrese la fecha del vuelo en dd/mm/aaaa:')
        
        for vuelo in vuelos:
            if vuelo[1].lower()==origen.lower() and vuelo[2].lower()==destino.lower() and vuelo[3].lower()==fecha.lower():
                print(e.azul('\nDATOS DEL VUELO:'))
                print(f'-Vuelo N°: {vuelo[0]}')
                print(f'-Origen: {vuelo[1]}')   
                print(f'-Destino: {vuelo[2]}') 
                print(f'-Fecha: {vuelo[3]}')      

                print('--------------------')
                i+=1
    
    if i==0: #ningun vuelo coincidio con los filtros
        print(e.rojo("\nNo hay vuelos con estas caracteristicas\n"))
        print(e.subtitulo("DESEA REALIZAR OTRA BUSQUEDA?"))
        print("1. Si\n2. No")
        opcion2 = err.validar_opcion(2)
        
        if opcion2==1:
            buscar_vuelos()
        else:
            mostrar_menus(0)
    mostrar_menus(1)
        

#Mostrar asientos 
def mostrar_asientos(vuelo_elegido):
    print(e.subtitulo('VUELO SELECCIONADO: ')+f'{vuelo_elegido[0]}')
    print(e.azul('-Origen: ')+f'{vuelo_elegido[1]}')
    print(e.azul('-Destino: ')+f'{vuelo_elegido[2]}')
    print('\n'+e.subtitulo('GRILLA DE ASIENTOS'))
    print(e.azul('-Asientos totales: ')+f'{vuelo_elegido[6]}')
    print(e.azul('-Asientos disponibles: ')+f'{vuelo_elegido[5]}\n')
    print("--Parte delantera--")
    print("    1  2  3  4\n")
    for i,fila in zip(indicesAsientos,vuelo_elegido[4]): #vuelo[4] es la matriz de asientos
        print(f"{i}  {fila}")
    print("--Parte trasera--")
    
    
def mostrar_vuelos():
    os.system('cls')
    print(e.titulo('VUELOS DISPONIBLES')+'\n')
    for vuelo in vuelos:
        #este lo conservo porque optimiza mas el codigo que muchas llamadas a la funcion e.azul
        print(f"- {{0}}Vuelo N°:{{1}} {vuelo[0]}, {{0}}Origen:{{1}} {vuelo[1]}, {{0}}Destino:{{1}} {vuelo[2]}, {{0}}Fecha:{{1}} {vuelo[3]}, {{0}}Asientos disponibles:{{1}} {vuelo[5]}, {{0}}Asientos totales:{{1}} {vuelo[6]}".format(e.estilo['azul'],e.estilo['reset']))
    
    mostrar_menus(1) #preguntar si muestra asientos
        
def comprar_pasajes(vuelo_elegido):
    bool = False
    os.system('cls') 
    print(e.titulo('1- SELECCIONE EL ASIENTO QUE DESEE')+'\n')
    mostrar_asientos(vuelo_elegido)
    
    while True:
        try:
            asiento_elegido=(input(e.datos('Ingrese la letra de la fila:')), int(input(e.datos('Ingrese el numero de columna:'))))
            
            #valido que la fila sea un str y la columna un int
            if asiento_elegido[0].isnumeric() or not isinstance(asiento_elegido[0], str) or not isinstance(asiento_elegido[1], int):
                raise ValueError
            
            #valido que la fila exista y que la columna este entre el 1 y el 4
            if asiento_elegido[0] not in indicesAsientos[:(vuelo_elegido[6]//4)] or asiento_elegido[1]<1 or asiento_elegido[1]>4:
                raise err.ErrorAsiento("Este asiento no existe, elija uno valido")
            
            
                            #matriz_asientos -> busco la fila (indice igual al indice de letra) -> busco la columna (-1 porque empieza en 0)
            estado_asiento= vuelo_elegido[4][indicesAsientos.index(asiento_elegido[0])][asiento_elegido[1]-1] #valor del asiento seleccionado
            
            #valido que no este ocupado
            if estado_asiento==1:
                raise err.ErrorAsiento("El asiento esta ocupado, por favor seleccione otro")
            
            #si todo lo anterior es valido
            break
        
        except ValueError:
            print(e.error("Error, la fila debe ser una letra y la columna un numero"))
            
        except err.ErrorAsiento as error:
            print(e.error(error))
    
    
    print('\n'+e.titulo('2- GESTION DE PAGO')+'\n')
    
    print(e.subtitulo('DATOS DE LA TARJETA'))
    n_tarjeta=err.validar_int('Numero de tarjeta:')
    cvv_tarjeta = err.validar_int('CVV:')
    nombre_tarjeta = err.validar_str('Nombre del titular (como figura en la tarjeta):')
    dni_titular = err.validar_int('DNI del titular:')
    
    print(f'\nPRECIO FINAL: ${vuelo_elegido[7]}')
    print('\n'+e.subtitulo('CONFIRMAR RESERVA?'))
    print('1. Si\n2. No')
    opcion= err.validar_opcion(2)
    
    if opcion==1:
        #pongo el asiento como ocupado
        vuelo_elegido[4][indicesAsientos.index(asiento_elegido[0])][asiento_elegido[1]-1]=1
        #resto uno a asientos disponibles
        vuelo_elegido[5]-=1
        #guardo el vuelo elegido y la tupla de asiento
        reservas.append([vuelo_elegido, asiento_elegido])
        mostrar_resumen(vuelo_elegido, asiento_elegido, n_tarjeta, nombre_tarjeta, dni_titular)
    else:
        os.system('cls')
        print('Compra cancelada!')
        mostrar_menus(0)
    
def mostrar_resumen(vuelo_elegido, asiento_elegido, n_tarjeta, nombre_tarjeta, dni_titular):
    os.system('cls')
    print(e.titulo('MUCHAS GRACIAS POR ELEGIRNOS!!')+'\n')
    print(e.subtitulo('**DETALLES DE LA COMPRA**'))
    
    print(e.azul('DETALLES DEL VUELO:'))
    print(f'-Vuelo N°: {vuelo_elegido[0]}')
    print(f'-Origen: {vuelo_elegido[1]}')   
    print(f'-Destino: {vuelo_elegido[2]}') 
    print(f'-Fecha: {vuelo_elegido[3]}')
    
    print('\n'+e.azul('DETALLES DEL ASIENTO:'))
    print(f'-Fila: {asiento_elegido[0]}')
    print(f'-Columna: {asiento_elegido[1]}')
    
    print('\n'+e.azul('DETALLES DEL PAGO:'))
    print(f'-Numero de compra #{r.randint(20000,22000)}')
    print(f'-Precio total ${vuelo_elegido[7]}')
    print(f'-Numero tarjeta: {n_tarjeta}')
    print(f'-Nombre del titular: {nombre_tarjeta}')
    print(f'-DNI del titular: {dni_titular}')
    
    print(e.subtitulo("\nDESEA IMPRIMIR SU RECIBO DE COMPRA?"))
    print("1. Si\n2. No")
    opcion = err.validar_opcion(2)
    
    if opcion==1:
        with open ("recibo.txt", "w") as archivo:
            texto_boleta = tw.dedent(generar_boleta(vuelo_elegido, asiento_elegido, n_tarjeta, nombre_tarjeta, dni_titular))
            archivo.write(texto_boleta)
    
    mostrar_menus(2)

#Cancelar reservas
def cancelar_reserva():
    if len(reservas)==0:
        print(e.error("\nNo hay reservas hechas por este usuario\n"))
        mostrar_menus(2)
    else:
        os.system('cls')
        print(e.titulo('VUELOS RESERVADOS\n'))
        for reserva in reservas:
            print(e.azul('DETALLES DEL VUELO:'))
            print(f'-Vuelo N°: {reserva[0][0]}')
            print(f'-Origen: {reserva[0][1]}')   
            print(f'-Destino: {reserva[0][2]}') 
            print(f'-Fecha: {reserva[0][3]}')
            
            print('\n'+e.subtitulo('DETALLES DEL ASIENTO:'))
            print(f'-Fila: {reserva[1][0]}')
            print(f'-Columna: {reserva[1][1]}')
            
            print('--------------------')
            
        print(e.subtitulo("ESTÁ SEGURO DE QUERER CANCELAR UNA DE ESTAS RESERVAS?"))
        print("1. Si\n2. No")
        opcion = err.validar_opcion(2)
        if opcion==1:
            vuelo_cancelado= err.validar_vuelo(reservas, "Ingrese el numero del vuelo del que desea cancelar la reserva:",2)
            for reserva in reservas:
                if reserva[0][0]==vuelo_cancelado:
                    #pongo el asiento en desocupado
                    reserva[0][4][indicesAsientos.index(reserva[1][0])][reserva[1][1]-1]=0
                    
                    #aumento la cantidad de asientos disponibles
                    reserva[0][5]+=1
                    
                    #quito el vuelo de la listas de reservas
                    reservas.remove(reserva)
                    
                    print(e.titulo("\nRESERVA CANCELADA!!"))
                    mostrar_menus(2)  
        else:
            mostrar_menus(0)
        
        
            
                

#DECLARACIONES
menu = f'''
{e.subtitulo('MENU PRINCIPAL')}
1 - Busqueda filtrada
2 - Mostrar vuelos disponibles
3 - Cancelar reserva
4 - Salir
'''

paises = [
    "Estados Unidos",
    "Canadá",
    "México",
    "Brasil",
    "Argentina",
    "Reino Unido",
    "Francia",
    "Alemania",
    "Italia",
    "España",
    "China",
    "Japón",
    "India",
    "Australia",
    "Rusia",
    "Sudáfrica",
    "Nigeria",
    "Egipto",
    "Turquía",
    "Corea del Sur"
]
fechas = [
    '30/04/2024', '31/06/2024', '15/08/2024', '20/10/2024', '25/12/2024',
    '05/02/2025', '10/04/2025', '20/06/2025', '15/08/2025', '30/10/2025',
    '25/12/2025', '20/02/2026', '15/04/2026', '10/06/2026', '05/08/2026',
    '20/10/2026', '15/12/2026', '10/02/2027', '05/04/2027', '30/06/2027'
]
opcionesAsientos= [60,80,100] #multiplos de 4
indicesAsientos=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] #no importa que no necesite tantos indices de asientos, cuando utilice ZIP utilizara solo los que necesite

#MAIN
vuelos = generar_vuelos()
reservas=[] #lista de listas, va a tener sublistas con [indice_vuelo, tupla asiento]
mostrar_menus(0)