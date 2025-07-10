import pygame
from funciones import *
from constantes import *
from recursos import *
from modulo_recursos.imagenes import *


def dibujar_menu(fondomenu, pantalla, fuente,COLOR_OPCIONES, RADIO_BORDES, titulo):
    pantalla.blit(fondomenu, [0, 0])

    opciones = {
        'opcion_jugar': pygame.draw.rect(pantalla, COLOR_OPCIONES,
                    pygame.Rect(235, 240, 310, 70), border_radius=RADIO_BORDES),
        'opcion_ranking': pygame.draw.rect(pantalla, COLOR_OPCIONES,
                    pygame.Rect(244, 330, 290, 50), border_radius=RADIO_BORDES),
        'opcion_salir': pygame.draw.rect(pantalla, COLOR_OPCIONES,
                    pygame.Rect(244, 400, 290, 50), border_radius=RADIO_BORDES)
    }
    pantalla.blit(titulo, (183, 30))

    texto_jugar = fuente.render("Jugar", True,  (0, 0, 0), None)
    texto_jugar_rect = texto_jugar.get_rect(center=opciones['opcion_jugar'].center)
    texto_ranking = fuente.render("Ranking", True,  (0, 0, 0), None)
    texto_ranking_rect = texto_jugar.get_rect(center=opciones['opcion_ranking'].center)
    texto_salir = fuente.render('Salir', True, (0, 0, 0), None)
    texto_salir_rect = texto_salir.get_rect(center=opciones['opcion_salir'].center)

    pantalla.blit(texto_jugar, texto_jugar_rect)
    pantalla.blit(texto_ranking, texto_ranking_rect)
    pantalla.blit(texto_salir, texto_salir_rect)
    return opciones

def dibujar_ingreso(fondomenu, pantalla, fuente, COLOR_TEXTOS, COLOR_OPCIONES,RADIO_BORDES, nombre):
    pantalla.blit(fondomenu, [0, 0])
    texto_aviso = fuente.render('Ingrese su nombre', True, COLOR_TEXTOS)
    texto_enviar = fuente.render('Enviar', True, COLOR_TEXTOS)
    texto_nombre = fuente.render(nombre, True, COLOR_TEXTOS)

    opciones = {
        'texto_aviso': pantalla.blit(texto_aviso, (260, 100)),
        'recuadro_juego': pygame.draw.rect(pantalla, COLOR_OPCIONES, pygame.Rect(189, 162, 380, 90), border_radius = RADIO_BORDES),
        'opcion_enviar': pygame.draw.rect(pantalla, COLOR_OPCIONES, pygame.Rect(189, 272, 165, 40), border_radius = RADIO_BORDES)
    }

    nombre_rect = texto_nombre.get_rect(center = opciones['recuadro_juego'].center)
    enviar_rect = texto_enviar.get_rect(center = opciones['opcion_enviar'].center)
    pantalla.blit(texto_nombre, nombre_rect)
    pantalla.blit(texto_enviar, enviar_rect)

    return opciones

def dibujar_boton_terminar(pantalla, COLOR_OPCIONES, RADIO_BORDES, COLOR_TEXTOS):
    opcion_terminar = pygame.draw.rect(pantalla, COLOR_OPCIONES, pygame.Rect(650, 43, 110, 40), border_radius=RADIO_BORDES)
    texto_terminar = fuente.render('Terminar', True, COLOR_TEXTOS)
    texto_terminar_rect = texto_terminar.get_rect(center = opcion_terminar.center)
    pantalla.blit(texto_terminar, texto_terminar_rect)
    return opcion_terminar

def dibujar_terminado(pantalla, fondomenu, COLOR_TEXTOS, usuario):
    pantalla.blit(fondomenu, (0, 0))
    pantalla.blit(terminaste, (200, 100))
    texto_puntaje = f'Score: {usuario['puntuacion']}'
    puntaje = fuente.render(texto_puntaje, True, COLOR_TEXTOS)
    pantalla.blit(puntaje, (350, 270))

    rect_volver = pygame.draw.rect(pantalla, COLOR_RECUADRO, pygame.Rect(600, 410, 160, 45), border_radius=RADIO_BORDES)
    texto_volver = fuente.render('Ver Ranking', True, COLOR_BLANCO)
    texto_rect = texto_volver.get_rect(center=rect_volver.center)
    pantalla.blit(texto_volver, texto_rect)
    return texto_rect


def dibujar_pilas(pilas, pantalla, imagendorso):
    for i, pila in enumerate(pilas):
        x_vacia = 100 + i * 90
        if len(pila) == 0:
            pantalla.blit(cargarcartas, (x_vacia, POSICION_INICIAL))
        for carta in pila:
            if carta['girada']:
                carta['imagen'] = pygame.transform.scale(carta['imagen'], TAMAÑO_CARTA)
                pantalla.blit(carta['imagen'], carta['rect'].topleft)
            else:
                pantalla.blit(imagendorso, carta['rect'].topleft)

def dibujar_mazo(pantalla, mazo_reserva, mazo_visible, rect_mazo_reserva):
    if len(mazo_visible) == 0:
        if len(mazo_reserva) > 0:
            ultima_carta_reserva = mazo_reserva[-1]
            ultima_carta_reserva['girada'] = False
            pantalla.blit(imagendorso, rect_mazo_reserva)
        else:
            pantalla.blit(cargarcartas, (100, 25))
    else:
        if len(mazo_reserva) > 0:
            ultima_carta_reserva = mazo_reserva[-1]
            ultima_carta_reserva['girada'] = False
            pantalla.blit(imagendorso, (100, 25))
        else:
            pantalla.blit(cargarcartas, (100, 25))
        ultima_carta_visible = mazo_visible[-1]
        ultima_carta_visible['girada'] = True
        ultima_carta_visible['rect'] = pygame.Rect(180, 25, 80, 115) # Posición visible a la derecha
        pantalla.blit(ultima_carta_visible['imagen'], ultima_carta_visible['rect'].topleft)

def dibujar_bases(bases, pantalla):
    for i, base in enumerate(bases):
        x_base = 300 + (i * 85)
        if len(base) == 0:
            pantalla.blit(baseimagen, (x_base, 25))
        else:
            ultima_carta = base[-1]
            ultima_carta['girada'] = True
            ultima_carta['rect'] = pygame.Rect(x_base, 25, 75, 110) # Posición visible a la derecha
            pantalla.blit(ultima_carta['imagen'], ultima_carta['rect'].topleft)


    
def dibujar_temporizador(minutos, segundos):
    temporizador_texto = fuente.render('Tiempo', True, (0, 0, 0))
    pantalla.blit(temporizador_texto, (15, 30))
    if minutos < 10:
        minutos_texto = f'0{minutos}:'
        minutos_texto_render = fuente.render(minutos_texto, True, (0, 0, 0))
        pantalla.blit(minutos_texto_render, (15, 60))
    else:
        minutos_texto_render = fuente.render(str(minutos), True, (0, 0, 0))
        pantalla.blit(minutos_texto_render, (15, 60))

    if segundos < 10:
        segundos_texto = f'0{segundos}'
        segundos_texto_render = fuente.render(segundos_texto, True, (0, 0, 0))
        pantalla.blit(segundos_texto_render, (60, 60))
    else:
        segundos_texto_render = fuente.render(str(segundos), True, (0, 0, 0))
        pantalla.blit(segundos_texto_render, (60, 60))
    
def dibujar_puntaje(usuario):
    texto_puntaje = fuente.render('Score', True, (0, 0, 0))
    puntajes = fuente.render(f'{usuario['puntuacion']}', True, (0, 0, 0))
    pantalla.blit(texto_puntaje, (15, 90))
    pantalla.blit(puntajes, (30, 110))

def dibujar_ranking():
    pantalla.blit(fondoranking, (0, 0))
    pantalla.blit(imagenranking, (230, 15))
    recuadro = pygame.Surface((555, 340))
    recuadro.set_alpha(150)  # 0 (totalmente transparente) a 255 (opaco)
    recuadro.fill((COLOR_RECUADRO))  # Color RGB sin alpha
    pantalla.blit(recuadro, (125, 115))

    rect_volver = pygame.draw.rect(pantalla, COLOR_RECUADRO, pygame.Rect(685, 410, 100, 45), border_radius=RADIO_BORDES)
    texto_volver = fuente.render('Volver', True, COLOR_BLANCO)
    texto_rect = texto_volver.get_rect(center=rect_volver.center)
    pantalla.blit(texto_volver, texto_rect)
    dibujar_columnas()
    dibujar_tabla_ranking()
    return texto_rect

def dibujar_tabla_ranking():
    ranking = ordenar_ranking('ranking.csv')
    x_usuario_nombre = 140
    x_usuario_puntaje = 395
    y_usuarios = 150
    espacio_y = 30
    for usuario in ranking:
        texto_nombre = fuente.render(usuario['nombre'], True, COLOR_BLANCO)
        texto_puntuacion = fuente.render(usuario['puntuacion'], True, COLOR_BLANCO)
        pantalla.blit(texto_nombre, (x_usuario_nombre, y_usuarios))
        pantalla.blit(texto_puntuacion, (x_usuario_puntaje, y_usuarios))
        y_usuarios += espacio_y

def dibujar_columnas():
    columnas = ('Nombre', 'Puntaje')
    x_columnas = 140
    y_columnas = 120
    espacio_columnas = 255
    for columna in columnas:
        texto = fuente.render(columna, True, COLOR_BLANCO)
        pantalla.blit(texto, (x_columnas, y_columnas))
        x_columnas += espacio_columnas

        

def dibujar_pantalla_juego(pantalla, pilas, bases,mazo_reserva, mazo_visible, rect_mazo_reserva, minutos, segundos, usuario):
    dibujar_pilas(pilas, pantalla, imagendorso)
    dibujar_mazo(pantalla, mazo_reserva, mazo_visible, rect_mazo_reserva)
    dibujar_bases(bases, pantalla)
    dibujar_temporizador(minutos, segundos)
    dibujar_puntaje(usuario)

def dibujar_seleccion(pantalla, carta_seleccionada):
    texto = ''
    if carta_seleccionada == None:
        texto_seleccion = fuente.render('Sin Seleccion', True, (200, 0, 0))
    else:
        texto_seleccion = fuente.render('Seleccionada', True, (COLOR_TEXTOS))
    pantalla.blit(texto_seleccion, (630, 0))