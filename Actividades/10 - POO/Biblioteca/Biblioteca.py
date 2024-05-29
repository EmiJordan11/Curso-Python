from Libro import Libro
import estilo as es
import json

class Biblioteca():
    def __init__(self, libros):
        self.libros=libros
        
        
    def mostrar_libros(self, n): #utilizo el segundo parametro para distinguir entre mostrar los libros disponibles o todos los libros
        
        print(es.azul("LIBROS DISPONIBLES\n"))
        
        #pongo al final los que no esten disponibles
        self.libros.sort(key=lambda libro: not libro.disponible)
        
        if n==1:
            for i, libro in enumerate(self.libros):
                if libro.disponible:
                    print(f"{{0}}{{1}}{i+1}. Titulo:{{2}} {libro.titulo}, {{0}}{{1}}Autor:{{2}} {libro.autor}, {{0}}{{1}}Unidades:{{2}} {libro.unidades}".format(es.estilo['subrayado'], es.estilo['morado'], es.estilo['reset']))
        else:
            for i, libro in enumerate(self.libros):
                    print(f"{{0}}{{1}}{i+1}. Titulo:{{2}} {libro.titulo}, {{0}}{{1}}Autor:{{2}} {libro.autor}, {{0}}{{1}}Unidades:{{2}} {libro.unidades}".format(es.estilo['subrayado'], es.estilo['morado'], es.estilo['reset']))
                
    def prestar_libro(self, libro):
        libro.unidades-=1
        if libro.unidades==0:
            #pongo que no este disponible solo si es la ultima unidad que tengo
            libro.disponible=False 
        
    def recibir_libro(self, libro):
        libro.unidades+=1
        libro.disponible=True
    
    def crear_biblioteca_json(url):
        
        with open(url, "r") as archivo:
            libros_json = json.load(archivo)
            libros = [Libro(**libro) for libro in libros_json]
            return Biblioteca(libros)
        
    
    def guardar_base_libros(self):
        libros_json = [libro.serializar() for libro in self.libros]
        
        with open("libros3.json", "w") as archivo:
            json.dump(libros_json, archivo, indent=4)
        
        print("Datos guardados en 'libros3.json'!")