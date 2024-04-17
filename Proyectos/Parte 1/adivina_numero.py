import os
from random import *

#MODULOS
#Mostrar menu
def mostrar_menu():
    os.system('cls')
    
    #Definiciones
    numero_bot = randint(1, 100)
    vidas=5
    
    print('\nBIENVENIDO')
    print('La máquina acaba de elegir un número que se encuentra entre el 1 al 100, trata de adivinar el número y gánale a la máquina, tienes 5 intentos, por cada intento se te dará una pista, Buena Suerte!!\n')
    definir_resultado(vidas, numero_bot)

#Menu volver a jugar
def volver_jugar():
    n=0
    print(menu2)
    while n<1 or n>2:
        n= int(input('Seleccione una opción: '))
            
    if n==1:
        mostrar_menu()
    else:
        print('Gracias por jugar!')
    
    
#Definir resultado
def definir_resultado(vidas, numero_bot):
    while vidas>0:
        #Selecciono un numero
        numero_pj = int(input('Elige un número: '))
        while numero_pj<1 or numero_pj>100:
            numero_pj = int(input('Seleccione una número válido: '))
            
        #Evaluo el resultado
        if numero_pj==numero_bot:
            os.system('cls')
            print('\nFelicidades, adivinaste el número elegido por la máquina!!!\n')
            volver_jugar()
        
        elif numero_pj<numero_bot:
            print('El número elegido por la máquina es mayor')
            
        else:
            print('El número elegido por la máquina es menor')
            
        vidas-=1
        print(f'Te quedan {vidas} vidas\n')
    
    os.system('cls')
    print(f'Perdiste :(, te quedaste sin vidas!!. El número elegido por la máquina era: {numero_bot}\n')        
    volver_jugar()
    
#DEFINICIONES
menu2='''
Quieres volver a jugar??
1- Sí
2- No
'''

#MAIN
os.system('cls')
mostrar_menu()