import os
import math
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils
pygame.init()
from Datos import *
from Ruleta import ruleta, dibujar_ruleta, dibuar_boton_ruleta
from Tablero import dibujar_tablero
from Jugadores import dibujar_jugador


# Definir la finestra
pygame.display.set_caption('Ruleta')

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
    global ultimo_angulo
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Obtener posición del clic
            mouse_x, mouse_y = event.pos
            # Comprobar si el clic está dentro del botón
            distancia = math.sqrt((mouse_x - boton_x_ruleta) ** 2 + (mouse_y - boton_y_ruleta) ** 2)
            if distancia <= boton_radio_ruleta:
                # Girar la ruleta
                ganador, ultimo_angulo = ruleta(ultimo_angulo)
                print(f"¡El número ganador es: {ganador}!")
    return True

# Fer càlculs
def app_run():
    pass

# Dibuixar
def app_draw():

    # Pintar el fons de blanc
    screen.fill(DARK_GREEN)

    # Dibuixar la graella
    utils.draw_grid(pygame, screen, 50)

    # Resol aquí l'exercici
    dibuar_boton_ruleta(RED)
    dibujar_ruleta(ultimo_angulo)  # Mostrar la ruleta al inicio
    dibujar_tablero()
    dibujar_jugador()

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()