import Datos as d
import pygame

def dibujar_scroll():
    rect_tuple = (d.scroll["x"], d.scroll["y"], d.scroll["width"], d.scroll["height"])
    pygame.draw.rect(d.screen, d.GRAY, rect_tuple)

    # Obtenir la posició "y" del cercle a partir del valor (percentage)
    circle_x = int(d.scroll["x"] + d.scroll["width"] / 2)
    circle_y = int(d.scroll["y"] + (d.scroll["percentage"] / 100) * d.scroll["height"])
    circle_tuple = (circle_x, circle_y)
    pygame.draw.circle(d.screen, d.BLACK, circle_tuple, d.scroll["radius"])

def actualizar_superficie():
    if len(d.historial) > 21:
        d.y_hist += 25
        d.surface = pygame.Surface((520, d.y_hist), pygame.SRCALPHA)
        d.surface.fill(d.DARK_GREEN)

def dibujar_historial():
    #SUPERFICIE HISTORIAL
    sub_surface = d.surface.subsurface(0, d.scroll["surface_offset"], d.surface.get_width(),540)
    d.screen.blit(sub_surface,(40,105))
    sub_surface.fill(d.DARK_GREEN)

    #SUPERPOSICION SUPERFICIE
    #FONDO TITULOS
    pygame.draw.rect(d.screen,d.DARK_GREEN,(40,40,520,65))
    #LINEA EXTERIOR
    pygame.draw.rect(d.screen,d.WHITE,(40,40,520,610),5)
    #LINEA INTERIOR
    pygame.draw.line(d.screen,d.WHITE,(115,40),(115,648),3)
    pygame.draw.line(d.screen,d.WHITE,(226,40),(226,648),3)
    pygame.draw.line(d.screen,d.WHITE,(380,40),(380,648),3)
    pygame.draw.line(d.screen,d.WHITE,(226,75),(558,75), 3)
    pygame.draw.line(d.screen,d.WHITE,(277,75),(277,648),2)
    pygame.draw.line(d.screen,d.WHITE,(328,75),(328,648),2)
    pygame.draw.line(d.screen,d.WHITE,(439,75),(439,648),2)
    pygame.draw.line(d.screen,d.WHITE,(498,75),(498,648),2)
    pygame.draw.line(d.screen,d.WHITE,(40,105),(558,105),3)
    #TEXTOS
    texto = d.arial20.render("Turno",True,d.WHITE)
    d.screen.blit(texto,(50,63))
    texto = d.arial20.render("Resultado",True, d.WHITE)
    d.screen.blit(texto,(123,63))
    texto = d.arial20.render("Credito", True, d.WHITE)
    d.screen.blit(texto,(233, 50))
    texto = d.arial20.render("Apuesta", True, d.WHITE)
    d.screen.blit(texto, (388, 50))
    texto = d.arial20.render("N", True, d.WHITE)
    d.screen.blit(texto, (233, 82))
    texto = d.arial20.render("L", True, d.WHITE)
    d.screen.blit(texto, (284, 82))
    texto = d.arial20.render("A", True, d.WHITE)
    d.screen.blit(texto, (335, 82))
    texto = d.arial20.render("N", True, d.WHITE)
    d.screen.blit(texto, (387, 82))
    texto = d.arial20.render("L", True, d.WHITE)
    d.screen.blit(texto, (447, 82))
    texto = d.arial20.render("A", True, d.WHITE)
    d.screen.blit(texto,(505, 82))
    #DATOS HISTORIAL
    y_pos = 0
    for i in range(0,len(d.historial)):
        texto = d.arial20b.render(d.historial[i]["turno"], True, d.WHITE)
        d.surface.blit(texto, (10, y_pos + 5))
        texto = d.arial20b.render(d.historial[i]["resultado"], True, d.WHITE)
        d.surface.blit(texto, (80, y_pos + 5))
        texto = d.arial15b.render(d.historial[i]["credito"]["N"], True, d.WHITE)
        d.surface.blit(texto, (190, y_pos + 8))
        texto = d.arial15b.render(d.historial[i]["credito"]["L"], True, d.WHITE)
        d.surface.blit(texto, (242, y_pos + 8))
        texto = d.arial15b.render(d.historial[i]["credito"]["A"], True, d.WHITE)
        d.surface.blit(texto, (293, y_pos + 8))
        texto = d.arial15b.render(d.historial[i]["apuesta"]["N"], True, d.WHITE)
        d.surface.blit(texto, (344, y_pos + 8))
        texto = d.arial15b.render(d.historial[i]["apuesta"]["L"], True, d.WHITE)
        d.surface.blit(texto, (404, y_pos + 8))
        texto = d.arial15b.render(d.historial[i]["apuesta"]["A"], True, d.WHITE)
        d.surface.blit(texto, (463, y_pos + 8))
        pygame.draw.line(d.surface,d.WHITE,(0,y_pos+25),(520,y_pos+25),1)
        y_pos += 25

def dibujar_boton_historial(texto,color):
    pygame.draw.rect(d.screen, color, (d.boton_historial["x"], d.boton_historial["y"], d.boton_historial["width"], d.boton_historial["height"]))
    pygame.draw.rect(d.screen, d.GOLDEN, (d.boton_historial["x"], d.boton_historial["y"], d.boton_historial["width"], d.boton_historial["height"]), 5)
    if texto == True:
        texto = d.arial55.render("Mostrar Historial", True, d.WHITE)
        texto_rect = texto.get_rect()
        texto_rect.center = (300,775)
        d.screen.blit(texto, texto_rect)
    if texto == False:
        texto = d.arial55.render("Mostrar Ruleta", True, d.WHITE)
        texto_rect = texto.get_rect()
        texto_rect.center = (300,775)
        d.screen.blit(texto, texto_rect)
