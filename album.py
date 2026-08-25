

class Album():
    def __init__(self, titulo, anio):
        self.titulo = titulo
        self.anio = anio
        self.canciones = []

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)

        print(f"{cancion.titulo} fue asociada"
            f" al album {self.titulo}")
        
    def mostrar_info(self):
        print("\n ---Playlist ---")
        print(f"Nombre:  {self.titulo}")
        print(f"Año:  {self.anio}")
        print("canciones: ")

        if len(self.canciones) == 0:
            print("no tiene canciones registradas")
        else:
            for cancion in self.canciones:
                print(f"- {cancion.titulo}"
                      f"- {cancion.genero}")