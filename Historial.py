from Datos import *


def dibujar_scroll():
    rect_tuple = (scroll["x"], scroll["y"], scroll["width"], scroll["height"])
    pygame.draw.rect(screen, GRAY, rect_tuple)

    # Obtenir la posició "y" del cercle a partir del valor (percentage)
    circle_x = int(scroll["x"] + scroll["width"] / 2)
    circle_y = int(scroll["y"] + (scroll["percentage"] / 100) * scroll["height"])
    circle_tuple = (circle_x, circle_y)
    pygame.draw.circle(screen, BLACK, circle_tuple, scroll["radius"])

def dibujar_historial():
    #SUPERFICIE HISTORIAL
    sub_surface = surface.subsurface(0, scroll["surface_offset"], surface.get_width(),540)
    screen.blit(sub_surface,(40,105))
    sub_surface.fill(DARK_GREEN)

    #SUPERPOSICION SUPERFICIE
    #FONDO TITULOS
    pygame.draw.rect(screen,DARK_GREEN,(40,40,520,65))
    #LINEA EXTERIOR
    pygame.draw.rect(screen,WHITE,(40,40,520,610),5)
    #LINEA INTERIOR
    pygame.draw.line(screen,WHITE,(115,40),(115,648),3)
    pygame.draw.line(screen,WHITE,(226,40),(226,648),3)
    pygame.draw.line(screen,WHITE,(380,40),(380,648),3)
    pygame.draw.line(screen,WHITE,(226,75),(558,75), 3)
    pygame.draw.line(screen,WHITE,(277,75),(277,648),2)
    pygame.draw.line(screen,WHITE,(328,75),(328,648),2)
    pygame.draw.line(screen,WHITE,(439,75),(439,648),2)
    pygame.draw.line(screen,WHITE,(498,75),(498,648),2)
    pygame.draw.line(screen,WHITE,(40,105),(558,105),3)
    #TEXTOS
    texto = arial20.render("Turno",True,WHITE)
    screen.blit(texto,(50,63))
    texto = arial20.render("Resultado",True, WHITE)
    screen.blit(texto,(123,63))
    texto = arial20.render("Credito", True, WHITE)
    screen.blit(texto,(233, 50))
    texto = arial20.render("Apuesta", True, WHITE)
    screen.blit(texto, (388, 50))
    texto = arial20.render("N", True, WHITE)
    screen.blit(texto, (233, 82))
    texto = arial20.render("L", True, WHITE)
    screen.blit(texto, (284, 82))
    texto = arial20.render("A", True, WHITE)
    screen.blit(texto, (335, 82))
    texto = arial20.render("N", True, WHITE)
    screen.blit(texto, (387, 82))
    texto = arial20.render("L", True, WHITE)
    screen.blit(texto, (447, 82))
    texto = arial20.render("A", True, WHITE)
    screen.blit(texto,(505, 82))

    #DATOS HISTORIAL
    y_pos = 0
    for i in range(0,len(historial)):
        texto = arial20b.render(historial[i]["turno"], True, WHITE)
        surface.blit(texto, (10, y_pos + 5))
        texto = arial20b.render(historial[i]["resultado"], True, WHITE)
        surface.blit(texto, (80, y_pos + 5))
        texto = arial15b.render(historial[i]["credito"]["N"], True, WHITE)
        surface.blit(texto, (190, y_pos + 8))
        texto = arial15b.render(historial[i]["credito"]["L"], True, WHITE)
        surface.blit(texto, (242, y_pos + 8))
        texto = arial15b.render(historial[i]["credito"]["A"], True, WHITE)
        surface.blit(texto, (293, y_pos + 8))
        texto = arial15b.render(historial[i]["apuesta"]["N"], True, WHITE)
        surface.blit(texto, (344, y_pos + 8))
        texto = arial15b.render(historial[i]["apuesta"]["L"], True, WHITE)
        surface.blit(texto, (404, y_pos + 8))
        texto = arial15b.render(historial[i]["apuesta"]["A"], True, WHITE)
        surface.blit(texto, (463, y_pos + 8))
        pygame.draw.line(surface,WHITE,(0,y_pos+25),(520,y_pos+25),1)
        y_pos += 25

def dibujar_boton_historial(texto,color):
    pygame.draw.rect(screen, color, (boton_historial["x"], boton_historial["y"], boton_historial["width"], boton_historial["height"]))
    pygame.draw.rect(screen, WHITE, (boton_historial["x"], boton_historial["y"], boton_historial["width"], boton_historial["height"]), 5)
    if texto == True:
        texto = arial55.render("Mostrar Historial", True, WHITE)
        texto_rect = texto.get_rect()
        texto_rect.center = (300,775)
        screen.blit(texto, texto_rect)
    if texto == False:
        texto = arial55.render("Mostrar Ruleta", True, WHITE)
        texto_rect = texto.get_rect()
        texto_rect.center = (300,775)
        screen.blit(texto, texto_rect)