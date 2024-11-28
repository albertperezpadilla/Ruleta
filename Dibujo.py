import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import utils
import ctypes
ctypes.windll.user32.SetProcessDPIAware()
pygame.init()

import Datos as d 
from Ruleta import ruleta, dibujar_ruleta, dibuar_boton_ruleta, dibujar_cuadro_ganador
from Tablero import dibujar_tablero
from Jugadores import dibujar_jugador, dibujar_turno_jug, distribuir_valores
from Historial import dibujar_boton_historial, dibujar_historial, dibujar_scroll, actualizar_superficie
import Apuestas as ap

ultimo_angulo = 0
ganador = ""
mostrar_historial = False
turno = 0

if ganador == "":
    for i in range(0,len(d.jugadores)):
        distribuir_valores(d.jugadores[str(i)]["saldo"])

# Definir la finestra
pygame.display.set_caption('Ruleta')

# Bucle de l'aplicació
def main():
    is_looping = True
    while is_looping:
        is_looping = app_events()
        app_run()
        app_draw()
        
        d.clock.tick(60) # Limitar a 60 FPS

    # Fora del bucle, tancar l'aplicació
    pygame.quit()
    sys.exit()

# Gestionar events
def app_events():
    mouse = d.mouse
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
        elif event.type == pygame.KEYDOWN:  # Se ha pulsado una tecla
            if event.key == pygame.K_SPACE:
                d.teclado["pressed"] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                d.teclado["pressed"] = False
    return True

# Fer càlculs
def app_run():
    global ganador, ultimo_angulo, turno, mostrar_historial
    # Obtenir la posició "y" del cercle a partir del valor (percentage)
    circle_center = {
        "x": int(d.scroll["x"] + d.scroll["width"] / 2),
        "y": int(d.scroll["y"] + (d.scroll["percentage"] / 100) * d.scroll["height"])
    }

    # Comprovar si el mouse ha fet click dins del cercle i iniciar l'arrossegament
    if len(d.historial) > 21:
        if d.mouse["pressed"] and not d.scroll["dragging"] and utils.is_point_in_circle(d.mouse, circle_center, d.scroll["radius"]):
            d.scroll["dragging"] = True

    # Si s'està arrossegant, actualitzar la posició del cercle
    
    if d.scroll["dragging"]:
        # Calcular el nou percentatge en funció de la posició dins de l'àrea de l'scroll
        relative_y = max(min(d.mouse["y"], d.scroll["y"] + d.scroll["height"]), d.scroll["y"])
        d.scroll["percentage"] = ((relative_y - d.scroll["y"]) / d.scroll["height"]) * 100
    
    # Comprobar si el clic está dentro del botón
    centro_circulo = {
        "x": d.boton_x_ruleta,
        "y": d.boton_y_ruleta
    }

    if d.mouse["pressed"] and not mostrar_historial and utils.is_point_in_circle(d.mouse, centro_circulo, d.boton_radio_ruleta):
        # Girar la ruleta
        d.mouse["pressed"]=False
        ganador, ultimo_angulo = ruleta(ultimo_angulo)
        turno += 1
        d.turno_jug = 0
        hist = {
            "turno":str(turno),
            "resultado":str(ganador),
            "credito":{
                "N":str(d.jugadores["0"]["saldo"]["total"]),
                "L":str(d.jugadores["1"]["saldo"]["total"]),
                "A":str(d.jugadores["2"]["saldo"]["total"])
            },
            "apuesta":{
                "N":str("acabar"),
                "L":str("acabar"),
                "A":str("acabar")
            }  
        }
        d.historial.append(hist)
        actualizar_superficie()
        for i in range(0,len(d.jugadores)):
            distribuir_valores(d.jugadores[str(i)]["saldo"])
        ap.fichas_naranja = []
        ap.fichas_lila = []
        ap.fichas_azul = []
        ap.fichas_dibujadas = [ap.fichas_naranja, ap.fichas_lila, ap.fichas_azul]
        return ganador

    if d.mouse["pressed"] and utils.is_point_in_rect(d.mouse, d.boton_historial):
        if mostrar_historial:
            mostrar_historial = False
        else:
            mostrar_historial = True
        d.mouse["pressed"] = False

    # Aturar l'arrossegament quan s'aixeca el botó del mouse
    if not d.mouse["pressed"]:
        d.scroll["dragging"] = False

    # Calcular la posició "y" de dibuix de la superfície
    d.scroll["surface_offset"] = int((d.scroll["percentage"] / 100) * (d.surface.get_height() - d.scroll["visible_height"]))
    
    if d.teclado["pressed"]:
        d.turno_jug +=1
        d.teclado["pressed"] = False

    

# Dibuixar
def app_draw():
    if d.jugadores["0"]["saldo"]["total"] == 0 and d.jugadores["1"]["saldo"]["total"] == 0 and d.jugadores["2"]["saldo"]["total"] == 0:
        d.screen.fill(d.BLACK)
        texto = d.arial150.render("HOUSE EDGE", True, d.RED)
        texto_rect = texto.get_rect()
        texto_rect.center = (900,450)
        d.screen.blit(texto,texto_rect)
    else:
        # Pintar el fons de blanc
        d.screen.fill(d.DARK_GREEN)
        pygame.draw.rect(d.screen,d.BROWN,(0,0,1800,900,),15)
        pygame.draw.rect(d.screen,d.GOLDEN,(0,0,1800,900,),5)

        # Dibuixar la graella
        utils.draw_grid(pygame, d.screen, 50)

        # Resol aquí l'exercici
        dibuar_boton_ruleta(d.RED)
        dibujar_ruleta(ultimo_angulo)  # Mostrar la ruleta al inicio
        dibujar_cuadro_ganador(ganador)
        dibujar_tablero()
        dibujar_jugador()
        dibujar_turno_jug()
        dibujar_boton_historial(True,d.RED)
        if mostrar_historial:
            dibujar_historial()
            dibujar_boton_historial(False,d.RED)
            if len(d.historial) > 21:
                dibujar_scroll()
        ap.dibujar_ficha_apuestas()
    # Actualitzar el dibuix a la finestra
    pygame.display.update()

if __name__ == "__main__":
    main()