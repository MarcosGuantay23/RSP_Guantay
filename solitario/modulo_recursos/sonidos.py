import pygame
pygame.mixer.init()


def reproducir_musica(estado_actual, estado_musica, volumen_sonidos, mute):
    estado_actualizado = None

    if estado_actual == 'menu' and estado_musica != 'menu':
        pygame.mixer.stop()
        pygame.mixer.music.load('solitario/musica/piano.ogg')
        pygame.mixer.music.set_volume(volumen_sonidos)

        pygame.mixer.music.play(-1)
        estado_actualizado = estado_actual
    elif estado_actual == 'juego' and estado_musica != 'juego':
        pygame.mixer.stop()
        pygame.mixer.music.load('solitario/musica/piano.ogg')
        pygame.mixer.music.set_volume(volumen_sonidos)

        pygame.mixer.music.play(-1)
        estado_actualizado = estado_actual
    else:
        estado_actualizado = estado_musica
    
    if mute:
        pygame.mixer.music.set_volume(0)
    else:
        pygame.mixer.music.set_volume(1)
    return estado_actualizado

def manejar_mute(mute):
    if not mute:
        mute = True
    else:
        mute = False
    return mute

def reproducir_sonido(sonidos, sonido, volumen_global, mute):
    if not mute:
        sonidos[sonido].set_volume(volumen_global)
        sonidos[sonido].play()