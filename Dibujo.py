import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils
from Datos import screen
pygame.init()
from Ruleta_2 import *

clock = pygame.time.Clock()
ultimo_angulo = 0

# Definir la finestra
pygame.display.set_caption('Window Title')

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