from Tamagotchi import Tamagotchi
import errores as e
import estilo as es
import os

def mostrar_menu(num_menu):
    
    if num_menu==1:
        #os.system('cls')
        print(menu) 
        opcion = e.validar_opcion(5)
        
        if opcion==1:
            os.system('cls')
            mascota1.alimentar()
        elif opcion==2:
            os.system('cls')
            mascota1.jugar()
        elif opcion==3:
            os.system('cls')
            mascota1.dormir()
        elif opcion==4:
            os.system('cls')
            mascota1.mostrar_estado()
        else:
            quit()
        mostrar_menu(1)
        
    else: 
        print("\nVolver al menu principal?")
        print("1. Si\n2. No")
        opcion = e.validar_opcion(2)
        
        if opcion==1:
            mostrar_menu(1)
        else:
            quit()
        
        
mascota1= Tamagotchi("godeto")       
menu = f"""
{es.subtitulo(f"Que deseas hacer con {mascota1.nombre}?")}

1. Alimentar
2. Jugar 
3. Dormir
4. Mostrar estado
5. Salir
"""

os.system('cls')
print(es.titulo("BIENVENIDO AL LUGAR DONDE PUEDES INTERACTUAR CON TU MASCOTA VIRTUAL"))
mostrar_menu(1)

        


