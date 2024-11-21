import math
import random
import pygame
import sys
from Datos import * 


def rotate_point(x, y, cx, cy):
    # Aplica las fórmulas de rotación
    x_new = cx + math.sqrt(2) / 2  * (x - cx) - math.sqrt(2) / 2 * (y - cy)
    y_new = cy + math.sqrt(2) / 2 * (x - cx) + math.sqrt(2) / 2  * (y - cy)
    return (x_new, y_new)

def dibujar_ruleta(angulo_actual):
    arial18 = pygame.font.SysFont("Arial", 18, True)

    #EXTERIOR
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

    #ROMBOS
    #HORIZONTAL/VERTICAL
    pygame.draw.polygon(
        screen,
        GOLDEN,
        [
            (CENTRO[0]     , CENTRO[1] - RADIO - 10), 
            (CENTRO[0] + 17, CENTRO[1] - RADIO - 20),
            (CENTRO[0]     , CENTRO[1] - RADIO - 30),
            (CENTRO[0] - 17, CENTRO[1] - RADIO - 20),
        ],
    )
    pygame.draw.polygon(
        screen,
        GOLDEN,
        [
            (CENTRO[0]     , CENTRO[1] + RADIO + 10), 
            (CENTRO[0] + 17, CENTRO[1] + RADIO + 20),
            (CENTRO[0]     , CENTRO[1] + RADIO + 30),
            (CENTRO[0] - 17, CENTRO[1] + RADIO + 20),
        ],
    )
    pygame.draw.polygon(
        screen,
        GOLDEN,
        [
            (CENTRO[0] - RADIO - 10, CENTRO[1]     ), 
            (CENTRO[0] - RADIO - 20, CENTRO[1] - 17),
            (CENTRO[0] - RADIO - 30, CENTRO[1]     ),
            (CENTRO[0] - RADIO - 20, CENTRO[1] + 17),
        ],
    )

    #DIAGONALES
    rombo = [
        (CENTRO[0]     , CENTRO[1] - RADIO - 12), 
        (CENTRO[0] + 17, CENTRO[1] - RADIO - 22),
        (CENTRO[0]     , CENTRO[1] - RADIO - 32),
        (CENTRO[0] - 17, CENTRO[1] - RADIO - 22),
    ]
    rombo_rotado = [rotate_point(x, y, CENTRO[0], CENTRO[1]) for x, y in rombo]
    pygame.draw.polygon(
        screen,
        GOLDEN,
        rombo_rotado,
    )
    rombo = [
        (CENTRO[0]     , CENTRO[1] + RADIO + 12), 
        (CENTRO[0] + 17, CENTRO[1] + RADIO + 22),
        (CENTRO[0]     , CENTRO[1] + RADIO + 32),
        (CENTRO[0] - 17, CENTRO[1] + RADIO + 22),
    ]
    rombo_rotado = [rotate_point(x, y, CENTRO[0], CENTRO[1]) for x, y in rombo]
    pygame.draw.polygon(
        screen,
        GOLDEN,
        rombo_rotado,
    )
    rombo = [
        (CENTRO[0] - RADIO - 12, CENTRO[1]     ), 
        (CENTRO[0] - RADIO - 22, CENTRO[1] - 17),
        (CENTRO[0] - RADIO - 32, CENTRO[1]     ),
        (CENTRO[0] - RADIO - 22, CENTRO[1] + 17),
    ]
    rombo_rotado = [rotate_point(x, y, CENTRO[0], CENTRO[1]) for x, y in rombo]
    pygame.draw.polygon(
        screen,
        GOLDEN,
        rombo_rotado,
    )
    rombo = [
        (CENTRO[0] + RADIO + 12, CENTRO[1]     ), 
        (CENTRO[0] + RADIO + 22, CENTRO[1] + 17),
        (CENTRO[0] + RADIO + 32, CENTRO[1]     ),
        (CENTRO[0] + RADIO + 22, CENTRO[1] - 17),
    ]
    rombo_rotado = [rotate_point(x, y, CENTRO[0], CENTRO[1]) for x, y in rombo]
    pygame.draw.polygon(
        screen,
        GOLDEN,
        rombo_rotado,
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
        pygame.draw.line(screen, 
            GOLDEN, 
            CENTRO, 
            punto_final, 
            3
        )

        #TEXTO
        angulo_texto = math.radians((360 / NUMEROS) * (idx + 0.5) + angulo_actual)
        x = CENTRO[0] + math.cos(angulo_texto) * (RADIO - 20)
        y = CENTRO[1] + math.sin(angulo_texto) * (RADIO - 20)
        texto = arial18.render(str(casilla["num"]), True, WHITE)
        screen.blit(texto, (x - texto.get_width() // 2, y - texto.get_height() // 2))

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

    #MARCADOR
    pygame.draw.polygon(
        screen,
        DARK_RED,
        [
            (CENTRO[0] + RADIO - 10, CENTRO[1]     ), 
            (CENTRO[0] + RADIO + 45, CENTRO[1] - 20), 
            (CENTRO[0] + RADIO + 45, CENTRO[1] + 20)
        ]
    )
    pygame.draw.polygon(
        screen,
        GOLDEN,
        [
            (CENTRO[0] + RADIO - 10, CENTRO[1]     ), 
            (CENTRO[0] + RADIO + 45, CENTRO[1] - 20), 
            (CENTRO[0] + RADIO + 45, CENTRO[1] + 20)
        ],
        3
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

def dibuar_boton_ruleta(color):
    pygame.draw.circle(
        screen, 
        color, 
        (
            boton_x_ruleta, 
            boton_y_ruleta
        ), 
        boton_radio_ruleta
    )
    pygame.draw.circle(
        screen, 
        GOLDEN, 
        (
            boton_x_ruleta, 
            boton_y_ruleta
        ), 
        boton_radio_ruleta,
        7
    )

    texto = arial18.render("GIRAR", True, WHITE)
    texto_rect = texto.get_rect(center=(boton_x_ruleta, boton_y_ruleta))
    screen.blit(texto, texto_rect)

def ruleta(angulo_inicial):
    global ultimo_angulo

    angulo = angulo_inicial
    velocidad = random.uniform(10, 20)
    desaceleracion = 0.04
    while velocidad > 0:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        angulo += velocidad
        velocidad -= desaceleracion

        dibujar_ruleta(angulo % 360)
        dibuar_boton_ruleta(DARK_RED)

        pygame.display.flip()
        pygame.time.delay(30)
    
    ultimo_angulo = angulo % 360  # Guardar el último ángulo
    ganador_idx = (int(NUMEROS - (ultimo_angulo) / (360 / NUMEROS))) % NUMEROS
    ganador = orden_ruleta[ganador_idx]
    return casillas[ganador]["num"], ultimo_angulo