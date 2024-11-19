#!/usr/bin/env python3

import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils

# Definir colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 128, 0)
BLUE  = (0, 0, 255)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0) 
GOLD = (255, 215, 0)

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((1800, 900))
pygame.display.set_caption('Ruleta de Casino')

# Listas y variables
casillas = {
    "0":{
        "num": 0,
        "color": "verde",
    },
    "1":{
        "num": 1,
        "color": "rojo",
    },
    "2":{
        "num": 2,
        "color": "negro",
    },
    "3":{
        "num": 3,
        "color": "rojo",
    },
    "4":{
        "num": 4,
        "color": "negro",
    },
    "5":{
        "num": 5,
        "color": "rojo",
    },
    "6":{
        "num": 6,
        "color": "negro",
    },
    "7":{
        "num": 7,
        "color": "rojo",
    },
    "8":{
        "num": 8,
        "color": "negro",
    },
    "9":{
        "num": 9,
        "color": "rojo",
    },
    "10":{
        "num": 10,
        "color": "negro",
    },
    "11":{
        "num": 11,
        "color": "negro",
    },
    "12":{
        "num": 12,
        "color": "rojo",
    },
    "13":{
        "num": 13,
        "color": "negro",
    },
    "14":{
        "num": 14,
        "color": "rojo",
    },
    "15":{
        "num": 15,
        "color": "negro",
    },
    "16":{
        "num": 16,
        "color": "rojo",
    },
    "17":{
        "num": 17,
        "color": "negro",
    },
    "18":{
        "num": 18,
        "color": "rojo",
    },
    "19":{
        "num": 19,
        "color": "rojo",
    },
    "20":{
        "num": 20,
        "color": "negro",
    },
    "21":{
        "num": 21,
        "color": "rojo",
    },
    "22":{
        "num": 22,
        "color": "negro",
    },
    "23":{
        "num": 23,
        "color": "rojo",
    },
    "24":{
        "num": 24,
        "color": "negro",
    },
    "25":{
        "num": 25,
        "color": "rojo",
    },
    "26":{
        "num": 26,
        "color": "negro",
    },
    "27":{
        "num": 27,
        "color": "rojo",
    },
    "28":{
        "num": 28,
        "color": "negro",
    },
    "29":{
        "num": 29,
        "color": "negro",
    },
    "30":{
        "num": 30,
        "color": "rojo",
    },
    "31":{
        "num": 31,
        "color": "negro",
    },
    "32":{
        "num": 32,
        "color": "rojo",
    },
    "33":{
        "num": 33,
        "color": "negro",
    },
    "34":{
        "num": 34,
        "color": "negro",
    },
    "35":{
        "num": 35,
        "color": "rojo",
    },
    "36":{
        "num": 36,
        "color": "negro",
    }
}
# Puntos tablero
puntos_tablero = [(470,50),(470,350)]
# Bucle de l'aplicació
def main():
    is_looping = True

    while is_looping:
        is_looping = app_events()
        app_run()
        app_draw()

        clock.tick(60) # Limitar a 60 FPS

    # Fora del bucle, tancar l'aplicació
    pygame.quit()
    sys.exit()

# Gestionar events
def app_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
    return True

# Fer càlculs (resol aquí l'exercici)
def app_run():
    pass

# Dibuixar
def app_draw():
    
    # Pintar el fons de blanc
    # QUITAR AL ACABAR EL TRABAJO 
    # screen.fill(DARK_GREEN)
    screen.fill(WHITE)

    # Dibuixar la graella
    utils.draw_grid(pygame, screen, 50)

    # Resol aquí l'exercici
    pygame.draw.circle(screen, GOLD, (260,260), 210, 5)
    pygame.draw.polygon(screen, BLACK, puntos_tablero,5)
    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()