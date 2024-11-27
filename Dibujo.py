import os
import math
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils
pygame.init()

from Datos import *
from Ruleta import ruleta, dibujar_ruleta, dibuar_boton_ruleta, dibujar_cuadro_ganador
from Tablero import dibujar_tablero
from Jugadores import dibujar_jugador
from Historial import dibujar_boton_historial, dibujar_historial, dibujar_scroll

# !!!!sonido_ruleta.play()!!!!
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
    global mouse
    mouse_inside = pygame.mouse.get_focused()  # El ratolí està dins de la finestra?

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Botó tancar finestra
            return False
        elif event.type == pygame.MOUSEMOTION:
            if mouse_inside:
                mouse["x"], mouse["y"] = event.pos
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse["pressed"] = True
            mouse["x"], mouse["y"] = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse["pressed"] = False
            mouse["x"], mouse["y"] = -1, -1
            print("El ratón fue soltado.")
    return True

# Fer càlculs
def app_run():
    global ultimo_angulo, scroll, mostrar_historial, turno, ganador, mouse

    # Obtenir la posició "y" del cercle a partir del valor (percentage)
    circle_center = {
        "x": int(scroll["x"] + scroll["width"] / 2),
        "y": int(scroll["y"] + (scroll["percentage"] / 100) * scroll["height"])
    }

    # Comprovar si el mouse ha fet click dins del cercle i iniciar l'arrossegament
    if len(historial) > 21:
        if mouse["pressed"] and not scroll["dragging"] and utils.is_point_in_circle(mouse, circle_center, scroll["radius"]):
            scroll["dragging"] = True

    # Si s'està arrossegant, actualitzar la posició del cercle
    
    if scroll["dragging"]:
        # Calcular el nou percentatge en funció de la posició dins de l'àrea de l'scroll
        relative_y = max(min(mouse["y"], scroll["y"] + scroll["height"]), scroll["y"])
        scroll["percentage"] = ((relative_y - scroll["y"]) / scroll["height"]) * 100
    
    # Comprobar si el clic está dentro del botón
    centro_circulo = {
        "x": boton_x_ruleta,
        "y": boton_y_ruleta
    }

    if mouse["pressed"] and not mostrar_historial and utils.is_point_in_circle(mouse, centro_circulo, boton_radio_ruleta):
        # Girar la ruleta
        mouse["pressed"]=False
        ganador, ultimo_angulo = ruleta(ultimo_angulo)
        turno += 1
        hist = {
            "turno":str(turno),
            "resultado":str(ganador),
            "credito":{
                "N":str(jugadores["0"]["saldo"]["total"]),
                "L":str(jugadores["1"]["saldo"]["total"]),
                "A":str(jugadores["2"]["saldo"]["total"])
            },
            "apuesta":{
                "N":str("acabar"),
                "L":str("acabar"),
                "A":str("acabar")
            }  
        }
        historial.append(hist)
        return ganador

    if mouse["pressed"] and utils.is_point_in_rect(mouse, boton_historial):
        if mostrar_historial:
            mostrar_historial = False
        else:
            mostrar_historial = True
        mouse["pressed"] = False

    # Aturar l'arrossegament quan s'aixeca el botó del mouse
    if not mouse["pressed"]:
        scroll["dragging"] = False

    # Calcular la posició "y" de dibuix de la superfície
    scroll["surface_offset"] = int((scroll["percentage"] / 100) * (surface.get_height() - scroll["visible_height"]))


# Dibuixar
def app_draw():
    if jugadores["0"]["saldo"]["total"] == 0 and jugadores["1"]["saldo"]["total"] == 0 and jugadores["2"]["saldo"]["total"] == 0:
        screen.fill(BLACK)
        texto = arial150.render("HOUSE EDGE", True, RED)
        texto_rect = texto.get_rect()
        texto_rect.center = (900,450)
        screen.blit(texto,texto_rect)
    else:
        # Pintar el fons de blanc
        screen.fill(DARK_GREEN)
        pygame.draw.rect(screen,BROWN,(0,0,1800,900,),15)
        pygame.draw.rect(screen,GOLDEN,(0,0,1800,900,),5)

        # Dibuixar la graella
        #utils.draw_grid(pygame, screen, 50)

        # Resol aquí l'exercici
        dibuar_boton_ruleta(RED)
        dibujar_ruleta(ultimo_angulo)  # Mostrar la ruleta al inicio
        dibujar_cuadro_ganador(ganador)
        dibujar_tablero()
        dibujar_jugador()
        dibujar_boton_historial(True,RED)
        if mostrar_historial:
            dibujar_historial()
            dibujar_boton_historial(False,RED)
            if len(historial) > 21:
                dibujar_scroll()


    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()