
from funciones import *
from puntajes import *
from recursos import *
from modulo_recursos.sonidos import *

def detectar_carta_pila(pilas, pos_mouse):
    pila_valida = False
    for pila in pilas:
        for carta in pila:
            if carta['rect'].collidepoint(pos_mouse):
                if carta['girada']:
                    pila_valida = True
    return pila_valida

def detectar_carta_base(bases, pos_mouse):
    base_valida = False
    for base in bases:
        if len(base) > 0:
            ultima_carta_base = base[-1]
            if ultima_carta_base['rect'].collidepoint(pos_mouse):
                base_valida = True
    return base_valida

def detectar_carta_mazo_visible(mazo_visible, pos_mouse):
    carta_valida = False
    if len(mazo_visible) > 0:
        ultima_carta_baraja = mazo_visible[-1]
        if ultima_carta_baraja['rect'].collidepoint(pos_mouse):
            carta_valida = True
    return carta_valida

def devolver_pila_cartas(pilas, pos_mouse, rects_pilas_vacias):
    pila_a_devolver = None
    for i, pila in enumerate(pilas):
        if len(pila) > 0:
            for carta in pila:
                if carta['rect'].collidepoint(pos_mouse):
                    pila_a_devolver = i
        else:
            if rects_pilas_vacias[i].collidepoint(pos_mouse):
                pila_a_devolver = i
    return pila_a_devolver

def devolver_base_cartas(bases, pos_mouse, rects_bases_vacias):
    base_a_devolver = None
    for i, base in enumerate(bases):
        if len(base) > 0:
            ultima_carta_base = base[-1]
            if ultima_carta_base['rect'].collidepoint(pos_mouse):
                base_a_devolver = i
        else:
            if rects_bases_vacias[i].collidepoint(pos_mouse):
                base_a_devolver = i
    return base_a_devolver

def generar_carta(origen, ubicacion, indice):
    carta_seleccionada = {'origen': origen,
                        'ubicacion_referencia': ubicacion,
                        'grupo_cartas': [],
                        'indice_carta': indice}
    return carta_seleccionada


def seleccionar_cartas_pila(pilas, pos_mouse, carta_seleccionada):
    if not carta_seleccionada:
        for pila in pilas:
            for i, carta in enumerate(pila):
                if carta['rect'].collidepoint(pos_mouse):
                    if carta['girada']:
                        carta_seleccionada = {
                            'origen': 'pila',
                            'ubicacion_referencia': pila,
                            'grupo_cartas': [],
                            'indice_carta': i
                            }
                        
                        for j in range(i, len(pila)):
                            carta_seleccionada['grupo_cartas'].append(pila[j])
    else:
        for carta in carta_seleccionada['grupo_cartas']:
            if carta['rect'].collidepoint(pos_mouse):
                carta_seleccionada = None
    return carta_seleccionada

def seleccionar_carta_mazo_visible(mazo_visible, pos_mouse, carta_seleccionada):
    if not carta_seleccionada:
        for i, carta in enumerate(mazo_visible):
            if carta['rect'].collidepoint(pos_mouse):
                carta_seleccionada = generar_carta('mazo', mazo_visible, i)
                carta_seleccionada['grupo_cartas'].append(mazo_visible[i])
    return carta_seleccionada



def enviar_carta_pila(carta_seleccionada, pilas, bases, pos_mouse, rects_pilas_vacias, rect_bases_vacias, usuario, mute):
    pila_seleccionada = devolver_pila_cartas(pilas, pos_mouse, rects_pilas_vacias)
    if pila_seleccionada == None:
        base_seleccionada = devolver_base_cartas(bases, pos_mouse, rect_bases_vacias)
        if base_seleccionada != None:
            if esta_base_vacia(bases[base_seleccionada]):
                if validar_carta_base(carta_seleccionada):
                    carta = carta_seleccionada['grupo_cartas'][0]
                    if carta['valor'] == 1:
                        base_nueva = [carta]
                        bases[base_seleccionada] = base_nueva
                        quitar_cartas(carta_seleccionada, 'pila', usuario)
                        sumar_puntos_base(usuario)
                        reproducir_sonido(sonidos, 'basesonido', VOLUMEN_GLOBAL, mute)
            else:
                carta_pila = carta_seleccionada['grupo_cartas'][-1]
                ultima_carta_base = bases[base_seleccionada][-1]
                if validar_carta(carta_pila, ultima_carta_base, 'base'):
                    bases[base_seleccionada].append(carta_pila)
                    quitar_cartas(carta_seleccionada, 'pila', usuario)
                    sumar_puntos_base(usuario)
                    reproducir_sonido(sonidos, 'basesonido', VOLUMEN_GLOBAL, mute)

    if pila_seleccionada != None:
        if esta_pila_vacia(pilas[pila_seleccionada]):
            primer_carta = carta_seleccionada['grupo_cartas'][0]
            if primer_carta['valor'] == 10:
                for carta in carta_seleccionada['grupo_cartas']:
                    pilas[pila_seleccionada].append(carta)
                quitar_cartas(carta_seleccionada, 'pila', usuario)
        elif validar_carta(carta_seleccionada['grupo_cartas'][0], pilas[pila_seleccionada][-1], 'pila'):
            for carta in carta_seleccionada['grupo_cartas']:
                pilas[pila_seleccionada].append(carta)
                quitar_cartas(carta_seleccionada, 'pila', usuario)
    return None

def enviar_carta_mazo(carta_seleccionada, pilas, bases, pos_mouse, rects_pilas_vacias, rect_bases_vacias, usuario, mute):
    pila_seleccionada = devolver_pila_cartas(pilas, pos_mouse, rects_pilas_vacias)
    carta = carta_seleccionada['grupo_cartas'][0]
    if pila_seleccionada == None:
        base_seleccionada = devolver_base_cartas(bases, pos_mouse, rect_bases_vacias)
        if base_seleccionada != None:
            if esta_base_vacia(bases[base_seleccionada]):
                if validar_carta_base(carta_seleccionada):
                    if carta['valor'] == 1:
                        base_nueva = [carta]
                        bases[base_seleccionada] = base_nueva
                        quitar_cartas(carta_seleccionada, 'mazo', usuario)
                        sumar_puntos_base(usuario)
                        reproducir_sonido(sonidos, 'basesonido', VOLUMEN_GLOBAL, mute)
            else:
                ultima_carta_base = bases[base_seleccionada][-1]
                if validar_carta(carta, ultima_carta_base, 'base'):
                    bases[base_seleccionada].append(carta)
                    quitar_cartas(carta_seleccionada, 'mazo', usuario)
                    sumar_puntos_base(usuario)
                    reproducir_sonido(sonidos, 'basesonido', VOLUMEN_GLOBAL, mute)

    if pila_seleccionada != None:
        if esta_pila_vacia(pilas[pila_seleccionada]):
            if carta['valor'] == 10:
                pilas[pila_seleccionada].append(carta)
                quitar_cartas(carta_seleccionada, 'mazo', usuario)
                sumar_puntos_comunes(usuario)
        elif validar_carta(carta, pilas[pila_seleccionada][-1], 'pila'):
            pilas[pila_seleccionada].append(carta)
            quitar_cartas(carta_seleccionada, 'mazo', usuario)
            sumar_puntos_comunes(usuario)
    return None


def quitar_cartas(carta_seleccionada, ubicacion, usuario):
    if ubicacion == 'pila':
        ubicacion_carta = len(carta_seleccionada['ubicacion_referencia'])
        for i in range(ubicacion_carta-1, carta_seleccionada['indice_carta']-1, -1):
            carta_seleccionada['ubicacion_referencia'].pop(i)
        if not esta_pila_vacia(carta_seleccionada['ubicacion_referencia']):
            if not carta_seleccionada['ubicacion_referencia'][-1]['girada']:
                sumar_puntos_comunes(usuario)
                carta_seleccionada['ubicacion_referencia'][-1]['girada'] = True
    elif ubicacion == 'mazo':
        carta_seleccionada['ubicacion_referencia'].pop()

def esta_pila_vacia(pila):
    return len(pila) == 0

def esta_base_vacia(base):
    return len(base) == 0

def validar_carta_base(carta_seleccionada):
    return len(carta_seleccionada['grupo_cartas']) == 1