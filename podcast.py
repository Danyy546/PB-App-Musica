from contenido import Contenido

class Podcast(Contenido):

    def __init__(self, titulo, duracion, categoria, num_episodio):
        super().__init__(titulo, duracion)
        self.categoria = categoria
        self.num_episodio = num_episodio

    def reproducir(self):
        print(f"Reproduciendo podcast {self.titulo}" 
              f" -Episodio {self.num_episodio}")

    def mostrar_informacion(self):
        print("\n ---Podcast---")
        print(f"Titulo: {self.titulo}")
        print(f"Duracion {self.duracion}")
        print(f"Categoria {self.categoria}")
        print(f"Episodio {self.num_episodio}")