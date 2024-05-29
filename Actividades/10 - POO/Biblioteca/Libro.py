class Libro():
    def __init__(self, titulo, autor, anio_publicacion, unidades):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.disponible = True
        self.unidades = unidades
        
    def serializar(self):
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "anio_publicacion": self.anio_publicacion,
            "unidades": self.unidades
        }