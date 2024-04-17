import os
from random import *
#MODULOS
#Mostrar menu
def mostrar_menu():
    print(menu1)
    seleccion = int(input('Elección: '))
    while seleccion<1 or seleccion>3:
        seleccion = int(input('Seleccione una opcion válida: '))
    
    definir_ganador(seleccion)

#Defino ganador
def definir_ganador(eleccion_pj):
    n=0
    eleccion_bot = randint(1,3)
    
    #Empate
    if eleccion_bot==eleccion_pj:
        os.system('cls')
        print('Empate!! Vuelve a elegir')
        mostrar_menu()
        
    #Gana PJ
    elif (eleccion_pj==1 and eleccion_bot==3) or (eleccion_pj==2 and eleccion_bot==1) or (eleccion_pj==3 and eleccion_bot==2):
        os.system('cls')
        print(f'TU: {opciones[eleccion_pj-1]} > BOT: {opciones[eleccion_bot-1]}\n')
        print('Felidades, lograste vencer a la máquina!!\n')
        print(menu2)
        
        while n<1 or n>2:
            n= int(input('Seleccione una opción: '))
        
        if n==1:
            os.system('cls')
            mostrar_menu()

        
    #Gana bot
    else:
        os.system('cls')
        print(f'TU: {opciones[eleccion_pj-1]} < BOT: {opciones[eleccion_bot-1]}\n')
        print('Perdiste :(, mejor suerte la próxima\n')
        print(menu2)
        
        while n<1 or n>2:
            n= int(input('Seleccione una opción: '))
        
        if n==1:
            os.system('cls')
            mostrar_menu()
    
    
    
    
#DEFINICIONES
seleccion=0
opciones = ('Piedra', 'Papel', 'Tijera')
menu1 = '''
SELECCIONE UNA DE LAS OPCIONES Y TRATA DE GANARLE A LA MÁQUINA
1- Piedra
2- Papel
3- Tijera
'''
menu2='''
Quieres volver a jugar??
1- Sí
2- No
'''

#MAIN
os.system('cls')
print('\nBIENVENIDO AL PIEDRAS, PAPEL O TIJERAS')
mostrar_menu()

    
