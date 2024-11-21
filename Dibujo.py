import os
import math
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils
from Datos import *
pygame.init()
from Ruleta import ruleta, dibujar_ruleta, ultimo_angulo, dibuar_boton_ruleta

clock = pygame.time.Clock()

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

    
    mouse_inside = pygame.mouse.get_focused() # El ratolí està dins de la finestra?

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                global ultimo_angulo
                ganador, ultimo_angulo = ruleta(ultimo_angulo)
                print(f"¡El número ganador es: {ganador}!")

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Obtener posición del clic
            mouse_x, mouse_y = event.pos
            # Comprobar si el clic está dentro del botón
            distancia = math.sqrt((mouse_x - boton_x_ruleta) ** 2 + (mouse_y - boton_y_ruleta) ** 2)
            if distancia <= boton_radio_ruleta:
                global boton_presionado
                
                boton_presionado = True
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
    screen.fill(WHITE)

    # Dibuixar la graella
    utils.draw_grid(pygame, screen, 50)

    # Resol aquí l'exercici
    dibujar_ruleta(ultimo_angulo)  # Mostrar la ruleta al inicio
    dibuar_boton_ruleta()

    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()