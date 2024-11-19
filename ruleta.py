#!/usr/bin/env python3

import math
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils
import random

# Definir colors
WHITE      = (255, 255, 255)
BLACK      = (0  , 0  , 0  )
RED        = (255, 0  , 0  )
GREEN      = (0  , 255, 0  )
BLUE       = (0  , 0  , 255)
PURPLE     = (128, 0  , 128)
ORANGE     = (255, 165, 0  ) 
YELLOW     = (255, 255, 0  )
BROWN      = (149, 95 , 32 )
GOLDEN     = (239, 184, 16 )
DARK_GREEN = (45 , 87 , 44 )
DARK_GRAY  = (51 , 47 , 44 )
GRAY       = (130, 130, 130)

pygame.init()
clock = pygame.time.Clock()

# Definir la finestra
screen = pygame.display.set_mode((1800, 900))
pygame.display.set_caption('Window Title')

#Listas y variables
casillas = {
    "0":  {"num":0,  "color":GREEN},
    "1":  {"num":1,  "color":RED  },
    "2":  {"num":2,  "color":BLACK},
    "3":  {"num":3,  "color":RED  },
    "4":  {"num":4,  "color":BLACK},
    "5":  {"num":5,  "color":RED  },
    "6":  {"num":6,  "color":BLACK},
    "7":  {"num":7,  "color":RED  },
    "8":  {"num":8,  "color":BLACK},
    "9":  {"num":9,  "color":RED  },
    "10": {"num":10, "color":BLACK},
    "11": {"num":11, "color":BLACK},
    "12": {"num":12, "color":RED  },
    "13": {"num":13, "color":BLACK},
    "14": {"num":14, "color":RED  },
    "15": {"num":15, "color":BLACK},
    "16": {"num":16, "color":RED  },
    "17": {"num":17, "color":BLACK},
    "18": {"num":18, "color":RED  },
    "19": {"num":19, "color":RED  },
    "20": {"num":20, "color":BLACK},
    "21": {"num":21, "color":RED  },
    "22": {"num":22, "color":BLACK},
    "23": {"num":23, "color":RED  },
    "24": {"num":24, "color":BLACK},
    "25": {"num":25, "color":RED  },
    "26": {"num":26, "color":BLACK},
    "27": {"num":27, "color":RED  },
    "28": {"num":28, "color":BLACK},
    "29": {"num":29, "color":BLACK},
    "30": {"num":30, "color":RED  },
    "31": {"num":31, "color":BLACK},
    "32": {"num":32, "color":RED  },
    "33": {"num":33, "color":BLACK},
    "34": {"num":34, "color":RED  },
    "35": {"num":35, "color":BLACK},
    "36": {"num":36, "color":RED  }
}

# Configuración de la ruleta
CENTRO = (260,260)
RADIO = 210
orden_ruleta = [
    "0" , "32", "15", "19", "4", "21" , 
    "2" , "25", "17", "34", "6", "27" ,
    "13", "36", "11", "30", "8", "23" , 
    "10", "5" , "24", "16", "33", "1" , 
    "20", "14", "31", "9" , "22", "18",
    "29", "7" , "28", "12", "35", "3" , 
    "26"
]
NUMEROS = len(orden_ruleta)
arial18 = pygame.font.SysFont("Arial", 18, True)
ultimo_angulo = 0

def dibujar_ruleta(angulo_actual):

    pygame.draw.circle(
        screen, 
        BROWN, 
        (CENTRO[0],CENTRO[1]), 
        RADIO+40,
    )

    pygame.draw.circle(
        screen, 
        GOLDEN, 
        (CENTRO[0],CENTRO[1]), 
        RADIO+47,
        8
    )

    #MARCADOR
    pygame.draw.polygon(
        screen,
        RED,
        [
            (CENTRO[0]     , CENTRO[1] - RADIO - 10), 
            (CENTRO[0] - 10, CENTRO[1] - RADIO - 30), 
            (CENTRO[0] + 10, CENTRO[1] - RADIO - 30)
        ]
    )
    pygame.draw.polygon(
        screen,
        BLACK,
        [
            (CENTRO[0]     , CENTRO[1] - RADIO - 10), 
            (CENTRO[0] - 10, CENTRO[1] - RADIO - 30), 
            (CENTRO[0] + 10, CENTRO[1] - RADIO - 30)
        ],
        3
    )

    #ROMBOS
    pygame.draw.polygon(
        screen,
        GOLDEN,
        [
            (CENTRO[0]     , CENTRO[1] + RADIO + 10), 
            (CENTRO[0] + 15, CENTRO[1] + RADIO + 20),
            (CENTRO[0]     , CENTRO[1] + RADIO + 30),
            (CENTRO[0] - 15, CENTRO[1] + RADIO + 20),
        ],
    )
    pygame.draw.polygon(
        screen,
        GOLDEN,
        [
            (CENTRO[0] + RADIO + 10, CENTRO[1]     ), 
            (CENTRO[0] + RADIO + 20, CENTRO[1] + 15),
            (CENTRO[0] + RADIO + 30, CENTRO[1]     ),
            (CENTRO[0] + RADIO + 20, CENTRO[1] - 15),
        ],
    )
    pygame.draw.polygon(
        screen,
        GOLDEN,
        [
            (CENTRO[0] - RADIO - 10, CENTRO[1]     ), 
            (CENTRO[0] - RADIO - 20, CENTRO[1] - 15),
            (CENTRO[0] - RADIO - 30, CENTRO[1]     ),
            (CENTRO[0] - RADIO - 20, CENTRO[1] + 15),
        ],
    )

    pygame.draw.line(
        screen, 
        GOLDEN, 
        (CENTRO[0]-89,CENTRO[1]+89), 
        (CENTRO[0]+89,CENTRO[1]-89),
        4
    )
    pygame.draw.line(
        screen, 
        GOLDEN, 
        (CENTRO[0]+89,CENTRO[1]+89), 
        (CENTRO[0]-89,CENTRO[1]-89),
        4
    )

    #SECTORES Y DECORACION
    for idx, key in enumerate(orden_ruleta):
        casilla = casillas[key]
        #ANGULO INICIO/FIN SECTOR
        angulo_inicio = math.radians((360 / NUMEROS) * idx + angulo_actual)
        angulo_fin = math.radians((360 / NUMEROS) * (idx + 1) + angulo_actual)
        color = casilla["color"]

        #SECTORES
        puntos = [
            CENTRO,
            (
                CENTRO[0] + math.cos(angulo_inicio) * RADIO,
                CENTRO[1] + math.sin(angulo_inicio) * RADIO,
            ),
            (
                CENTRO[0] + math.cos(angulo_fin) * RADIO,
                CENTRO[1] + math.sin(angulo_fin) * RADIO,
            ),
        ]
        pygame.draw.polygon(screen, color, puntos)

        #LINEA DIVISORA
        punto_final = (
            CENTRO[0] + math.cos(angulo_inicio) * RADIO,
            CENTRO[1] + math.sin(angulo_inicio) * RADIO,
        )
        pygame.draw.line(screen, GOLDEN, CENTRO, punto_final, 3)

        #TEXTO
        angulo_texto = math.radians((360 / NUMEROS) * (idx + 0.5) + angulo_actual)
        x = CENTRO[0] + math.cos(angulo_texto) * (RADIO - 20)
        y = CENTRO[1] + math.sin(angulo_texto) * (RADIO - 20)
        texto = arial18.render(str(casilla["num"]), True, WHITE)
        screen.blit(texto, (x - texto.get_width() // 2, y - texto.get_height() // 2))

    #BOLA RULETA
    pygame.draw.circle(
        screen, 
        WHITE, 
        (CENTRO[0],CENTRO[1]-150), 
        RADIO-200,
    )
    pygame.draw.circle(
        screen, 
        GRAY, 
        (CENTRO[0],CENTRO[1]-150), 
        RADIO-200,
        2
    )

    #BORDES 
    pygame.draw.circle(
        screen, 
        GOLDEN, 
        CENTRO, 
        RADIO+3, 
        6
    )
    pygame.draw.circle(
        screen, 
        GOLDEN, 
        CENTRO, 
        RADIO-35, 
        6
    )

    #INTERIOR RULETA
    #FONDO
    pygame.draw.circle(
        screen, 
        BROWN, 
        CENTRO, 
        RADIO-80,
    )

    #LINEAS
    #VERTICAL/HORIZONTAL
    pygame.draw.line(
        screen, 
        GOLDEN, 
        (CENTRO[0],CENTRO[1]+129), 
        (CENTRO[0],CENTRO[1]-129),
        3
    )
    pygame.draw.line(
        screen, 
        GOLDEN, 
        (CENTRO[0]+129,CENTRO[1]), 
        (CENTRO[0]-129,CENTRO[1]),
        3
    )
    #DIAGONALES
    pygame.draw.line(
        screen, 
        GOLDEN, 
        (CENTRO[0]-89,CENTRO[1]+89), 
        (CENTRO[0]+89,CENTRO[1]-89),
        4
    )
    pygame.draw.line(
        screen, 
        GOLDEN, 
        (CENTRO[0]+89,CENTRO[1]+89), 
        (CENTRO[0]-89,CENTRO[1]-89),
        4
    )

    #CENTRO
    pygame.draw.circle(
        screen, 
        GOLDEN, 
        CENTRO, 
        RADIO-180,
    )
    pygame.draw.circle(
        screen, 
        WHITE, 
        CENTRO, 
        RADIO-190,
        12
    )

    #BORDE
    pygame.draw.circle(
        screen, 
        GOLDEN, 
        CENTRO, 
        RADIO-80, 
        6
    )

def ruleta(angulo_inicial):
    angulo = angulo_inicial
    velocidad = random.uniform(5, 15)
    desaceleracion = 0.02

    while velocidad > 0:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        angulo += velocidad
        velocidad -= desaceleracion

        dibujar_ruleta(angulo % 360)
        pygame.display.flip()
        pygame.time.delay(30)

    global ultimo_angulo
    ultimo_angulo = angulo % 360  # Guardar el último ángulo
    ganador_idx = (int(NUMEROS - (ultimo_angulo) / (360 / NUMEROS))) % NUMEROS
    ganador = orden_ruleta[ganador_idx]
    return casillas[ganador]["num"]

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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ganador = ruleta(ultimo_angulo)
                print(f"¡El número ganador es: {ganador}!")
                print(f"Último ángulo: {ultimo_angulo:.2f}")
    return True

# Fer càlculs
def app_run():
    pass

# Dibuixar
def app_draw():
    global ultimo_angulo

    # Pintar el fons de blanc
    screen.fill(WHITE)

    # Dibuixar la graella
    utils.draw_grid(pygame, screen, 50)

    # Resol aquí l'exercici
    dibujar_ruleta(ultimo_angulo)  # Mostrar la ruleta al inicio

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()