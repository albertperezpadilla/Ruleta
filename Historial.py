from Datos import *

def dibujar_scroll():
    rect_tuple = (scroll["x"], scroll["y"], scroll["width"], scroll["height"])
    pygame.draw.rect(screen, GRAY, rect_tuple)

    # Obtenir la posició "y" del cercle a partir del valor (percentage)
    circle_x = int(scroll["x"] + scroll["width"] / 2)
    circle_y = int(scroll["y"] + (scroll["percentage"] / 100) * scroll["height"])
    circle_tuple = (circle_x, circle_y)
    pygame.draw.circle(screen, BLACK, circle_tuple, scroll["radius"])
    sub_surface = surface.subsurface((0, scroll["surface_offset"], surface.get_width(), scroll["visible_height"]))
    screen.blit(sub_surface, (40, 40))
    pygame.draw.rect(screen, WHITE, (40, 40, 520, 610), 5)
    y_pos = 10
    for i in range(len(historial)):
        text = arial40.render("> " + historial[i], True, WHITE)
        surface.blit(text, (10, y_pos))
        y_pos += 40


def dibujar_historial():
    pygame.draw.rect(screen, RED, (boton_historial["x"], boton_historial["y"], boton_historial["width"], boton_historial["height"]))
    pygame.draw.rect(screen, WHITE, (boton_historial["x"], boton_historial["y"], boton_historial["width"], boton_historial["height"]), 5)
    text = arial55.render("Mostrar Historial", True, WHITE)
    screen.blit(text, (100, 750))