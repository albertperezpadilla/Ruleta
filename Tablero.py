from Datos import *
import pygame


# Dibuixar
def dibujar_tablero():
    pos_x_tablero = 790
    pos_y_tablero = 150
    pos2_x_tablero = 870
    # Dibuixa 
    for i in range(0,len(casillas)-1):
        pygame.draw.rect(screen, casillas[str(i+1)]["color"], (casillas[str(i+1)]["pos_ini"][0], casillas[str(i+1)]["pos_ini"][1], 80, 100))
    pygame.draw.polygon(screen, WHITE, puntos_tablero,5)
    pygame.draw.polygon(screen, WHITE, puntos_0, 5)

    # Lineas horizontales
    for i in range(12):
        if i in (3,7):
            pygame.draw.line(screen, WHITE, (pos_x_tablero, 50), (pos_x_tablero, 550), 5)
        else:
            pygame.draw.line(screen, WHITE, (pos_x_tablero, 50), (pos_x_tablero, 350), 5)
        pos_x_tablero += 80
    
    # Lineas verticales
    for i in range(4):
        if i == 3:
            pygame.draw.line(screen, WHITE, (710, pos_y_tablero), (1670, pos_y_tablero), 5)
        else:
            pygame.draw.line(screen, WHITE, (710, pos_y_tablero), (1750, pos_y_tablero), 5)
        pygame.draw.line(screen, WHITE, (pos2_x_tablero, 450), (pos2_x_tablero, 550), 5)
        pos2_x_tablero += 80 * 4
        pos_y_tablero += 100
    
    # Numeros tablero
    for i in range(0,len(casillas)-1):
        text = arial55.render(str(casillas[str(i+1)]["num"]), True, WHITE)
        if len(str(casillas[str(i+1)]["num"])) == 1:
            screen.blit(text, (casillas[str(i+1)]["pos_ini"][0] + 25, (casillas[str(i+1)]["pos_ini"][1] + 20)))
        else:
            screen.blit(text, (casillas[str(i+1)]["pos_ini"][0] + 10, (casillas[str(i+1)]["pos_ini"][1] + 20)))
    text = arial55.render("0", True, WHITE)
    screen.blit(text, (630 + 25, 150 + 20))

    text = arial55.render("1ˢᵗ 12", True, WHITE)
    screen.blit(text, (790, 370))
    text = arial55.render("2ⁿᵈ 12", True, WHITE)
    screen.blit(text, (1110, 370))
    text = arial55.render("3ʳᵈ 12", True, WHITE)
    screen.blit(text, (1430, 370))

    text = arial40.render("1 to 18", True, WHITE)
    screen.blit(text, (730, 475))
    text = arial40.render("Even", True, WHITE)
    screen.blit(text, (905, 475))
    text = arial40.render("Odd", True, WHITE)
    screen.blit(text, (1390, 475))
    text = arial40.render("19 to 36", True, WHITE)
    screen.blit(text, (1515, 475))

    #ROMBOS
    pygame.draw.polygon(screen, RED, ((1050, 500), (1110, 470), (1170, 500), (1110, 530)))
    pygame.draw.polygon(screen, WHITE, ((1050, 500), (1110, 470), (1170, 500), (1110, 530)), 5)

    pygame.draw.polygon(screen, BLACK, ((1210, 500), (1270, 470), (1330, 500), (1270, 530)))
    pygame.draw.polygon(screen, WHITE, ((1210, 500), (1270, 470), (1330, 500), (1270, 530)), 5)
    text = arial35.render("2 to 1", True, WHITE)
    text_vertical = pygame.transform.rotate(text, 90)
    y = 55
    for i in range(3):
        screen.blit(text_vertical, (1690, y))
        y += 100