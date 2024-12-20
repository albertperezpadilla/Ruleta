import pygame
import math
import Datos as d


def distribuir_valores(diccionario):
    # Extraer el total y las denominaciones del diccionario
    total = diccionario["total"]
    denominaciones = sorted(int(k) for k in diccionario.keys() if k != "total")

    # Reiniciar los valores a cero
    for den in denominaciones:
        diccionario[str(den)] = 0

    # Paso 1: distribuir al menos una unidad por denominación si es posible
    for den in denominaciones:
        if total >= den:
            diccionario[str(den)] = 1
            total -= den

    # Paso 2: distribuir equitativamente las denominaciones de menor a mayor
    while total > 0:
        for den in denominaciones:
            if total >= den:
                diccionario[str(den)] += 1
                total -= den
            if total <= 0:
                break
    return diccionario

def posiciones_circulo(center, radius, num_points):
    positions = []
    for i in range(num_points):
        angle = math.radians((90 + 360 * i / num_points)+180)  # Ángulo en radianes
        x = center[0] + radius * math.cos(angle)  # Coordenada X
        y = center[1] + radius * math.sin(angle)  # Coordenada Y
        positions.append((x, y))
    return positions

def dibujar_ficha(x, y, valor, jugador, jugador2):
    #SECTORES
    for i in range(12):
        #ANGULO INICIO/FIN SECTOR
        angulo_inicio = math.radians((360 / 12) * i + 15)
        angulo_fin = math.radians((360 / 12) * (i + 1) +15)
        color = jugador if i % 2 == 0 else d.WHITE

        #SECTORES
        puntos = [
            (x,y),
            (
                x + math.cos(angulo_inicio) * 20,
                y + math.sin(angulo_inicio) * 20,
            ),
            (
                x + math.cos(angulo_fin) * 20,
                y + math.sin(angulo_fin) * 20,
            ),
        ]
        pygame.draw.polygon(d.screen, color, puntos)


    #CIRCULO EXTERIOR
    pygame.draw.circle(d.screen, jugador2, (x,y),22, 3)

    #CIRCULO INTERIOR
    pygame.draw.circle(d.screen, jugador2, (x,y),20-(25/4))

    #VALOR
    text = d.arial10.render(valor, True, d.BLACK)
    text_rect = text.get_rect(center=(x, y))
    d.screen.blit(text, text_rect)

def dibujar_jugador():
    x_jugadores = 600
    for i in range(0,len(d.jugadores)):
        pygame.draw.rect(
            d.screen,
            d.jugadores[str(i)]["color"]["1"],
            (
                x_jugadores,
                600,
                250,
                250
            ),
        )
        pygame.draw.rect(
            d.screen,
            d.jugadores[str(i)]["color"]["2"],
            (
                x_jugadores,
                600,
                250,
                250
            ),
            5
        )

        #NOMBRE JUGADOR
        texto = d.arial30.render(d.jugadores[str(i)]["jugador"], True, d.jugadores[str(i)]["color"]["2"])
        d.screen.blit(texto,(x_jugadores+10,610))
        pygame.draw.line(d.screen,d.jugadores[str(i)]["color"]["2"], (x_jugadores,645), (x_jugadores+248,645),3  )

        #FICHAS  
        pos = posiciones_circulo((x_jugadores+125,730),60,5)
        
        dibujar_ficha(pos[0][0],pos[0][1],"100",d.jugadores[str(i)]["color"]["1"],d.jugadores[str(i)]["color"]["2"])
        texto = d.arial15.render(str(d.jugadores[str(i)]["saldo"]["100"]), True, d.jugadores[str(i)]["color"]["2"])
        d.screen.blit(texto,(pos[0][0]+23,pos[0][1]-8))

        dibujar_ficha(pos[1][0],pos[1][1],"50",d.jugadores[str(i)]["color"]["1"],d.jugadores[str(i)]["color"]["2"])
        texto = d.arial15.render(str(d.jugadores[str(i)]["saldo"]["50"]), True, d.jugadores[str(i)]["color"]["2"])
        texto_rect = texto.get_rect()
        texto_rect.center = (pos[1][0],pos[1][1])
        d.screen.blit(texto,(texto_rect[0],texto_rect[1]+30))

        dibujar_ficha(pos[2][0],pos[2][1],"20",d.jugadores[str(i)]["color"]["1"],d.jugadores[str(i)]["color"]["2"])
        texto = d.arial15.render(str(d.jugadores[str(i)]["saldo"]["20"]), True, d.jugadores[str(i)]["color"]["2"])
        texto_rect = texto.get_rect()
        texto_rect.center = (pos[2][0],pos[2][1])
        d.screen.blit(texto,(texto_rect[0],texto_rect[1]+30))

        dibujar_ficha(pos[3][0],pos[3][1],"10",d.jugadores[str(i)]["color"]["1"],d.jugadores[str(i)]["color"]["2"])
        texto = d.arial15.render(str(d.jugadores[str(i)]["saldo"]["10"]), True, d.jugadores[str(i)]["color"]["2"])
        texto_rect = texto.get_rect()
        texto_rect.center = (pos[3][0],pos[3][1])
        d.screen.blit(texto,(texto_rect[0],texto_rect[1]+30))

        dibujar_ficha(pos[4][0],pos[4][1],"5",d.jugadores[str(i)]["color"]["1"],d.jugadores[str(i)]["color"]["2"])
        texto = d.arial15.render(str(d.jugadores[str(i)]["saldo"]["5"]), True, d.jugadores[str(i)]["color"]["2"])
        texto_rect = texto.get_rect()
        texto_rect.center = (pos[4][0],pos[4][1])
        d.screen.blit(texto,(texto_rect[0],texto_rect[1]+30))

        #TOTALS
        pygame.draw.line(d.screen,d.jugadores[str(i)]["color"]["2"], (x_jugadores,820), (x_jugadores+248,820),3  )
        texto = d.arial20.render("Total: "+str(d.jugadores[str(i)]["saldo"]["total"]), True, d.jugadores[str(i)]["color"]["2"])
        d.screen.blit(texto,(x_jugadores+10,825))

        x_jugadores += 300

def dibujar_turno_jug():
    if d.turno_jug == 0:
        pygame.draw.polygon(d.screen, d.DARK_ORANGE, ((810, 625), (835, 610), (835, 640)))
    elif d.turno_jug == 1:
        pygame.draw.polygon(d.screen, d.DARK_LILAC, ((1110, 625), (1135, 610), (1135, 640)))
    elif d.turno_jug == 2:
        pygame.draw.polygon(d.screen, d.DARK_BLUE, ((1410, 625), (1435, 610), (1435, 640)))
    else:
        d.turno_jug = 0