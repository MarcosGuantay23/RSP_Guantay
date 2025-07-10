import pygame
from constantes import *

cursor_nuevo = pygame.image.load('solitario/cartas/cursor_pointer.png')
cursor_nuevo = pygame.transform.scale(cursor_nuevo, (25, 25))
pygame.mouse.set_visible(False)
icon = pygame.image.load("solitario/cartas/diamante1.png") #Carga la imagen 
pygame.display.set_icon(icon) #Coloca el icono

fondomenu = pygame.image.load('solitario/cartas/fondojuego.png')
fondomenu= pygame.transform.scale(fondomenu, (800, 500))
fondojuego = pygame.image.load('solitario/cartas/fondojuego.png')
fondojuego = pygame.transform.scale(fondojuego, (800, 500))
fondoranking = pygame.image.load('solitario/cartas/fondojuego.png')
fondoranking = pygame.transform.scale(fondoranking, (800, 500))

titulo = pygame.image.load("solitario/cartas/solitarioTitulo.png")
titulo = pygame.transform.scale(titulo, (410, 250))
terminaste = pygame.image.load("solitario/cartas/terminaste.png")
terminaste = pygame.transform.scale(terminaste, (410, 250))
imagenranking = pygame.image.load("solitario/cartas/ranking.png")
imagenranking = pygame.transform.scale(imagenranking, (330, 80))
fuente = pygame.font.Font(None, 17)
volumen = pygame.image.load("solitario/cartas/MusicNotes.png")
volumen = pygame.transform.scale(volumen, (45, 45))

imagendorso = pygame.image.load('solitario/cartas/dorsocarta.png')
imagendorso = pygame.transform.scale(imagendorso, TAMAÑO_CARTA)
cargarcartas = pygame.image.load('solitario/cartas/dorsocarta.png')
cargarcartas = pygame.transform.scale(cargarcartas, TAMAÑO_CARTA)
baseimagen = pygame.image.load('solitario/cartas/dorsocarta.png')
baseimagen = pygame.transform.scale(baseimagen, TAMAÑO_CARTA)