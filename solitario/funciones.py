import random
import csv
import pygame
from modulo_recursos import *
from puntajes import *

def crear_usuario(nombre):
    """
    Crea el usuario con nombre y puntuacion
    """
    usuario = {
        "nombre": nombre,
        "puntuacion": 0
    }
    return usuario

def generar_baraja(palos, colores, maximo_valor):
    """
    Genera la baraja y la mezcla
    """
    baraja = []
    for palo in palos:
        for i in range(maximo_valor):
            if palo == 'corazon' or palo == 'diamante':
                carta = {
                    "palo": palo,
                    "valor": i+1,
                    "girada": False,
                    "color": colores[0],
                    "imagen": pygame.image.load(f'./solitario/cartas/{palo}{i+1}.png'),
                    "rect": pygame.Rect(0, 0, 71, 96)
                }
                baraja.append(carta)
            else:
                carta = {
                    "palo": palo,
                    "valor": i+1,
                    "girada": False,
                    "color": colores[1],
                    "imagen": pygame.image.load(f'./solitario/cartas/{palo}{i+1}.png'),
                    "rect": pygame.Rect(0, 0, 71, 96)
                }
                baraja.append(carta)

    random.shuffle(baraja)
    return baraja

def generar_mazo_reserva(baraja):
    """
    Genera el mazo de reserva/auxiliar
    """
    mazo_reserva = []
    for i in range(28, len(baraja)):
        mazo_reserva.append(baraja[i])
    for i in range(len(baraja)-1, 27, -1):
        baraja.pop(i)
    return mazo_reserva

def buscar_ultima_carta(lista, sublista):
    """
    Busca en una pila (lista) el indice indicado (busca desde el ultimo elemento)
    """
    ultima_carta = lista[sublista][-1]
    return ultima_carta

def final_juego(bases):
    """
    Evalua si el juego se pudo completar con las bases completadas (10 de cada palo)
    """
    finalizo = False
    bases_completadas = 0
    for i, base in enumerate(bases, 0):
        if base != None:
            ultima_carta = buscar_ultima_carta(bases, i)
            if ultima_carta['valor'] == 10:
                bases_completadas += 1

    if bases_completadas == 4:
        finalizo = True

    return finalizo

def generar_ranking(usuario):
    """
    Genera el archivo csv del ranking y los coloca correctamente"""
    with open('ranking.csv', 'a+', newline='') as archivo:
        writer = csv.writer(archivo)
        if archivo_esta_vacio(archivo):
            columnas = ['nombre', 'puntuacion']
            writer.writerow(columnas)

        archivo.seek(0)
        writer.writerow(
            [
            usuario['nombre'],
            usuario['puntuacion']
            ])

def ordenar_ranking(ruta):
    """
    Muestra el ranking
    """
    with open(ruta, 'a+') as archivo:  
        archivo.seek(0)
        ranking_archivo = csv.DictReader(archivo)
        ranking = []
        for usuario in ranking_archivo:
            ranking.append(usuario)
        for i in range(len(ranking)):
            for j in range(len(ranking)-1):
                if int(ranking[j]['puntuacion']) < int(ranking[j+1]['puntuacion']):
                    aux = ranking[j+1]
                    ranking[j+1] = ranking[j]
                    ranking[j] = aux
        return ranking

def archivo_esta_vacio(archivo):
    """
    verifica que el archivo ranking no esté vacio
    """
    vacio = False
    archivo.seek(0)
    if archivo.read().strip() == '':
        vacio = True
    return vacio

def distribuir_pilas(pilas, baraja):
    cant_cartas = 0
    cant_pilas = 1
    for i in range(len(pilas)):
        for j in range(cant_pilas):  
            carta = baraja[cant_cartas]
            carta['girada'] = False
            pilas[i].append(carta)
            cant_cartas += 1
            carta['rect'].topleft = (100 + (i * 90), 140 + (j * 30)) # 100 + (i * 90) el resultado de esto.     
        ultima_carta = len(pilas[i])-1
        pilas[i][ultima_carta]['girada'] = True
        cant_pilas += 1

def actualizar_pilas(pilas):
    for i, pila in enumerate(pilas):
        x = 100 + i * 90
        for j, carta in enumerate(pila):
            y = 140 + j * 30
            carta['rect'].topleft = (x, y)

def actualizar_bases(bases):
    for i, base in enumerate(bases):
        if base != None:
            x = 300 + (i * 85)
            y = 25
            ultima_carta_base = buscar_ultima_carta(bases, base)
            ultima_carta_base['rect'].topleft = (x, y)


def validar_carta(carta, ultima_carta, ubicacion):
    """
    Valida que la carta sea la que le sigue a una carta colocada
    """
    carta_valida = False
    if ubicacion == 'base':
        if carta['palo'] == ultima_carta['palo'] and carta['valor'] == ultima_carta['valor']+1:
            carta_valida = True
    elif ubicacion == 'pila':
        if carta['color'] != ultima_carta['color'] and carta['valor'] == ultima_carta['valor']-1:
            carta_valida = True
    return carta_valida

def generar_pilas_vacias():
    rects_pilas_vacias = []
    for i in range(7):  
        x = 100 + i * 90
        y = 140
        rect = pygame.Rect(x, y, 75, 110)  
        rects_pilas_vacias.append(rect)
    return rects_pilas_vacias

def generar_bases_vacias():
    rects_bases_vacias = []
    for i in range(4):
        x = 300 + (i * 85)
        y = 25
        rect = pygame.Rect(x, y, 75, 110)
        rects_bases_vacias.append(rect)
    return rects_bases_vacias