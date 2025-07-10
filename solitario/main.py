import pygame, sys
from constantes import *
from recursos import *
from funciones import *
from manejar_estados import *
from manejar_eventos import *
from modulo_recursos.sonidos import *
from modulo_recursos.imagenes import *

#Inicializaciones generales
estado_actual = 'menu'
estado_musica = None
baraja_generada = False
carta_seleccionada = None

# Datos de ejecución
nombre = ''
usuario = None
minutos = 0
segundos = 0
mute = False

seguir = True
while seguir:
    pos_mouse = pygame.mouse.get_pos()
    estado_musica = reproducir_musica(estado_actual, estado_musica, VOLUMEN_GLOBAL, mute)

    if estado_actual == 'menu':
        opciones_menu = dibujar_menu(fondomenu, pantalla, fuente, COLOR_OPCIONES, RADIO_BORDES, titulo)
    elif estado_actual == 'ranking':
        opcion_volver_ranking = dibujar_ranking()
    elif estado_actual == 'ingreso':
        opciones_ingreso = dibujar_ingreso(fondomenu, pantalla, fuente, COLOR_TEXTOS, COLOR_OPCIONES, RADIO_BORDES, nombre)
    elif estado_actual == 'juego':
        pantalla.blit(fondojuego, (0, 0))
        if not baraja_generada:
            baraja = generar_baraja(palos, colores, MAXIMO_VALOR)
            mazo_reserva = generar_mazo_reserva(baraja)
            bases = [[], [], [], []]
            mazo_visible = []
            distribuir_pilas(pilas, baraja)
            baraja_generada = True
        dibujar_pantalla_juego(pantalla, pilas, bases, mazo_reserva, mazo_visible, rect_mazo_reserva, minutos, segundos, usuario)
        opcion_terminar = dibujar_boton_terminar(pantalla, COLOR_OPCIONES, RADIO_BORDES, COLOR_TEXTOS)
        dibujar_seleccion(pantalla, carta_seleccionada) 
    elif estado_actual == 'terminado':
        opcion_volver_terminado = dibujar_terminado(pantalla, fondomenu, COLOR_TEXTOS, usuario)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                if boton_musica.collidepoint(pos_mouse):
                    mute = manejar_mute(mute)
                
                if estado_actual == 'menu':
                    if opciones_menu['opcion_jugar'].collidepoint(pos_mouse):
                        estado_actual = 'ingreso'
                        reproducir_sonido(sonidos, 'aceptar', VOLUMEN_GLOBAL, mute)
                    elif opciones_menu['opcion_ranking'].collidepoint(pos_mouse):
                        estado_actual = 'ranking'
                        reproducir_sonido(sonidos, 'aceptar', VOLUMEN_GLOBAL, mute)
                    elif opciones_menu['opcion_salir'].collidepoint(pos_mouse):
                        pygame.quit()
                        sys.exit()
                elif estado_actual == 'ranking':
                    if opcion_volver_ranking.collidepoint(pos_mouse):
                        estado_actual = 'menu'
                        reproducir_sonido(sonidos, 'aceptar', VOLUMEN_GLOBAL, mute)

                elif estado_actual == 'ingreso':
                    if opciones_ingreso['opcion_enviar'].collidepoint(pos_mouse):
                        if nombre.strip() != '':
                            usuario = crear_usuario(nombre)
                            estado_actual = 'juego'
                            reproducir_sonido(sonidos, 'aceptar', VOLUMEN_GLOBAL, mute)
                
                elif estado_actual == 'juego':
                    if opcion_terminar.collidepoint(pos_mouse):
                        estado_actual = 'terminado'
                        generar_ranking(usuario)

                    if rect_mazo_reserva.collidepoint(pos_mouse):
                        if len(mazo_reserva) > 0:
                            carta = mazo_reserva.pop()
                            carta['girada'] = True
                            carta['imagen'] = pygame.transform.scale(carta['imagen'], TAMAÑO_CARTA)
                            carta['rect'] = pygame.Rect(180, 25, 80, 115)
                            mazo_visible.append(carta)
                        else:
                            for carta in mazo_visible:
                                carta['girada'] = False
                                mazo_reserva.append(carta)
                            mazo_visible.clear()

                    if not carta_seleccionada:
                        if detectar_carta_pila(pilas, pos_mouse):
                            carta_seleccionada = seleccionar_cartas_pila(pilas, pos_mouse, carta_seleccionada)
                        elif detectar_carta_mazo_visible(mazo_visible, pos_mouse):
                            carta_seleccionada = seleccionar_carta_mazo_visible(mazo_visible, pos_mouse, carta_seleccionada)
                    elif carta_seleccionada and carta_seleccionada['origen'] == 'pila':
                        carta_seleccionada = enviar_carta_pila(carta_seleccionada, pilas, bases, pos_mouse, rects_pilas_vacias, rects_bases_vacias, usuario, mute)
                    elif carta_seleccionada and carta_seleccionada['origen'] == 'mazo':
                        carta_seleccionada = enviar_carta_mazo(carta_seleccionada, pilas, bases, pos_mouse, rects_pilas_vacias, rects_bases_vacias, usuario, mute)
                    actualizar_pilas(pilas)

                elif estado_actual == 'terminado':
                    if opcion_volver_terminado.collidepoint(pos_mouse):
                        estado_actual = 'ranking'



        if evento.type == pygame.KEYDOWN:
            if estado_actual == 'ingreso':
                if evento.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                else:
                    nombre += evento.unicode
                reproducir_sonido(sonidos, 'escribir', VOLUMEN_GLOBAL, mute)
                
        if evento.type == TEMPORIZADOR:
            if estado_actual == 'juego':
                segundos += 1
                if segundos == 60:
                    minutos += 1
                    segundos = 0
    
    
    clock.tick(60)
    boton_musica = pantalla.blit(volumen, (30, 430))    
    pantalla.blit(cursor_nuevo, pos_mouse)
    pygame.display.update()