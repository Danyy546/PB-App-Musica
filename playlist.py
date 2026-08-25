

class Playlist():
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.canciones = []

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)

        print(f"{cancion.titulo} fue asociada"
            f" a la playlist {self.nombre}")
            
    def eliminar_cancion(self, cancion):
        
        if cancion in self.canciones:
            self.canciones.remove(cancion)
            print(f"{cancion.titulo} fue removida"
              f" de la playlist {self.nombre}")
        else:
            print("Cancion no encontrada")

    def mostrar_info(self):
        print("\n ---Playlist ---")
        print(f"Nombre:  {self.nombre}")
        print(f"Descripcion:  {self.descripcion}")
        print("canciones: ")

        if len(self.canciones) == 0:
            print("no tiene canciones registradas")
        else:
            for cancion in self.canciones:
                print(f"- {cancion.titulo}"
                      f"- {cancion.genero}")


            