from contenido import Contenido

class Cancion(Contenido):

    def __init__(self, titulo, duracion, genero):
        super().__init__(titulo, duracion)
        self.genero = genero

    def reproducir(self):
        print(f"Reproduciendo la cancion... {self.titulo}")

    def mostrar_informacion(self):
        print("\n ---CANCION---")
        print(f"Título: {self.titulo}")
        print(f"Duración: {self.duracion}")
        print(f"Género: {self.genero}")