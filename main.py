from contenido import Contenido
from cancion import Cancion
from podcast import Podcast
from artista import Artista
from playlist import Playlist
from usuario import Usuario
from album import Album

def main():
    
    # CREAR CANCION
    cancion_uno = Cancion("Beat it",4.50, "Pop")
    cancion_dos = Cancion("Bad", 3.25, "Pop")

    # CREAR PODCAST
    podcast_uno = Podcast("Ultima luna", 35, "Comedia", 15)

    #CREAR ARTISTA

    nuevo_artista = Artista("Michael Jackson", "Pop")

    #ASOCIASR CANCIONES AL ARTISTA
    nuevo_artista.agregar_cancion(cancion_uno)
    nuevo_artista.agregar_cancion(cancion_dos)

    nuevo_artista.mostrar_informacion()

    #CREAR UNA PLAYLIST
    playlist1 = Playlist("Yooo", "la mejor playlist")

    #ASOCIAR CANCIONES A PLAYLIST
    playlist1.mostrar_info()
    playlist1.agregar_cancion(cancion_uno)
    playlist1.  agregar_cancion(cancion_dos)
    playlist1.mostrar_info()

    #CREAR USUARIO
    usuario1 = Usuario("Daniel", "danybravocea546@gmail.com", True)
    usuario1.crear_playlist(playlist1)
    usuario1.mostrar_info()

    #CREAR ALBUM
    album1 = Album("Bad", 1987)
    album1.agregar_cancion(cancion_uno)
    album1.agregar_cancion(cancion_dos)
    album1.mostrar_info()



if __name__=="__main__":
    main()