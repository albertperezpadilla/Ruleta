import pygame
from Datos import *


def dibujar_jugador():
    x_jugadores = 600
    for i in range(0,len(jugadores)):
        pygame.draw.rect(
            screen,
            jugadores[str(i)]["color"],
            (
                x_jugadores,
                600,
                250,
                250
            ),
        )
        pygame.draw.rect(
            screen,
            jugadores[str(i)]["color_2"],
            (
                x_jugadores,
                600,
                250,
                250
            ),
            5
        )

        texto = arial30.render(jugadores[str(i)]["jugador"], True, jugadores[str(i)]["color_2"])
        screen.blit(texto,(x_jugadores+10,610))

        pygame.draw.line(screen,jugadores[str(i)]["color_2"], (x_jugadores,645), (x_jugadores+248,645),3  )




        x_jugadores += 250 + 50
