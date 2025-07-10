import pygame
from constantes import *
from modulo_recursos import *
from funciones import generar_pilas_vacias, generar_bases_vacias

pygame.init()
pygame.mixer.init()

pantalla = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Solitario")
clock = pygame.time.Clock()

rect_mazo_reserva = pygame.Rect(100, 25, 80, 115)
rect_mazo_visible = pygame.Rect(180, 25, 80, 115)

rects_pilas_vacias = generar_pilas_vacias() # Acá voy a guardar en caso de que necesite verificar una pila vacía
rects_bases_vacias = generar_bases_vacias() # Acá voy a guardar los rects que verifican las colisiones de bases vacías

sonidos = {
    'aceptar': pygame.mixer.Sound('solitario/musica/piano.ogg'),
    'escribir': pygame.mixer.Sound('solitario/musica/piano.ogg'),
    'basesonido': pygame.mixer.Sound('solitario/musica/piano.ogg')
}


palos = ("corazon", "diamante", "pica", "trebol")
colores = ('rojo', 'negro')
pilas = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
]

