#imports
from Libro import Libro
from Biblioteca import Biblioteca
import os
import errores as e
import estilo as es

#definiciones
bibliotecas=[]

menu1 =f"""
{es.azul("BIENVENIDO")}

1. Crear una nueva Biblioteca
2. Trabajar con una biblioteca existente
3. Salir
"""

menu2=f"""
{es.naranja("Que operacion desea realizar?")}

1. Ver libros disponibles
2. Prestar un libro
3. Recibir un libro
4. Agregar libro
5. Eliminar libro
6. Guardar datos de los libros (archivo JSON)
7. Volver al menu principal
8. Salir
""" 

#FUNCIONES
def generar_bibliotecas_iniciales(url):
    biblioteca_inicial = Biblioteca.crear_biblioteca_json(url)
    bibliotecas.append(biblioteca_inicial)



def mostrar_menu(num_menu):
    
    #menu inicial (crear bibliteca o utilizar una existente)
    if num_menu==1:
        print(menu1)
        opcion=e.validar_opcion(3)
        
        if opcion==1:
            os.system('cls')
            print("Creando biblioteca...")
            url = e.validar_ruta()
            nueva_biblioteca = Biblioteca.crear_biblioteca_json(url)
            bibliotecas.append(nueva_biblioteca)
            print("\nBiblioteca creada con exito!")
            mostrar_menu(1)
        
        elif opcion==2:
            mostrar_menu(2)

        else:
            quit()
            
    #menu para seleccionar biblioteca
    elif num_menu==2:
        os.system('cls')
        print(f"\n{es.azul("BIBLIOTECAS DISPONIBLES")}")
        print("Con que biblioteca desea trabajar?\n")
        for i in range(len(bibliotecas)):
            print(f"- Biblioteca {i+1}")
        print("")
        opcion=e.validar_opcion(len(bibliotecas))
        os.system('cls')
        trabajar_con_biblioteca(bibliotecas[opcion-1])
        
        
       

def trabajar_con_biblioteca(biblioteca):
    print("\n--------------------------------------------------------------------------------------")
    print(es.recordatorio(f"\nUsted esta trabajando con: Biblioteca {bibliotecas.index(biblioteca)+1}"))
    print(menu2)
    opcion=e.validar_opcion(8)
    
    if opcion==1:
        os.system('cls')
        biblioteca.mostrar_libros(1)
        trabajar_con_biblioteca(biblioteca)
        
    elif opcion==2:
        os.system('cls')
        print(es.naranja("\nQue libro desea prestar?\n"))
        biblioteca.mostrar_libros(1)
        cant_libros_d= sum(1 for libro in biblioteca.libros if libro.disponible) #cuento los libros disponibles
        print("")
        indice_libro_elegido=e.validar_opcion(cant_libros_d) #limito la cantidad de opciones respecto al calculo anterior
        biblioteca.prestar_libro(biblioteca.libros[indice_libro_elegido-1])
        trabajar_con_biblioteca(biblioteca)
        
    elif opcion==3:
        os.system('cls')
        print(es.naranja("\nQue libro esta por recibir?\n"))
        biblioteca.mostrar_libros(0) #muestro tambien los que estan No disponible
        print("")
        indice_libro_elegido=e.validar_opcion(len(biblioteca.libros))
        biblioteca.recibir_libro(biblioteca.libros[indice_libro_elegido-1])
        trabajar_con_biblioteca(biblioteca)
        
    elif opcion==4:
        os.system('cls')
        print(es.naranja("\nINGRESE LOS DATOS DEL LIBRO QUE DESEA AGREGAR\n"))
        titulo = input(es.datos("Titulo:"))
        autor = input(es.datos("Autor:"))
        anio_publicacion = e.validar_int("Año de publicación:")
        unidades=e.validar_int("Cantidad de unidades:")
        libro_nuevo = Libro(titulo, autor, anio_publicacion, unidades)
        biblioteca.libros.append(libro_nuevo)
        print("\n Libro agregado a tu biblioteca!")
        trabajar_con_biblioteca(biblioteca)
    
    elif opcion==5:
        os.system('cls')
        print(es.naranja("\nSELECCIONE EL LIBRO QUE DESEE ELIMINAR\n"))
        biblioteca.mostrar_libros(0)
        print("")
        indice_libro_eliminado=e.validar_opcion(len(biblioteca.libros))
        print("Confirma la eliminacion de este libro?")
        print("1. Si\n2. No")
        opcion=e.validar_opcion(2)
        
        if opcion==1:
            biblioteca.libros.pop(indice_libro_eliminado-1)
            print("\nLibro eliminado!")
        else:
            print("Operacion cancelada!")
            
        trabajar_con_biblioteca(biblioteca)
        
    elif opcion==6:
        os.system('cls')
        print("Generando archivo...")
        biblioteca.guardar_base_libros()
        trabajar_con_biblioteca(biblioteca)
        
    elif opcion==7:
        os.system('cls')
        mostrar_menu(1)
        
    else:
        quit()
        

#MAIN

#genero las bibliotecas iniciales
generar_bibliotecas_iniciales("libros.json")
generar_bibliotecas_iniciales("libros2.json")

os.system('cls')
mostrar_menu(1)