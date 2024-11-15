import pygame
import math
import random
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ANCHO, ALTO = 800, 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ruleta de Casino")

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)

# Configuración de la ruleta
CENTRO = (ANCHO // 2, ALTO // 2)
RADIO = 200
NUMEROS = 37  # Del 0 al 36

# Crear los números y colores de la ruleta
numeros = list(range(NUMEROS))
colores = [ROJO if i % 2 == 0 else NEGRO for i in range(1, NUMEROS)]
colores.insert(0, VERDE)  # El número 0 es verde

# Fuente para texto
fuente = pygame.font.SysFont("Arial", 18)

# Dibujar la ruleta
def dibujar_ruleta(angulo_actual):
    VENTANA.fill(NEGRO)  # Limpiar pantalla
    for i in range(NUMEROS):
        # Calcular los ángulos de inicio y fin de cada sector
        angulo_inicio = math.radians((360 / NUMEROS) * i + angulo_actual)
        angulo_fin = math.radians((360 / NUMEROS) * (i + 1) + angulo_actual)
        color = colores[i]

        # Dibujar un sector de la ruleta
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
        pygame.draw.polygon(VENTANA, color, puntos)

        # Dibujar el texto del número
        angulo_texto = math.radians((360 / NUMEROS) * (i + 0.5) + angulo_actual)
        x = CENTRO[0] + math.cos(angulo_texto) * (RADIO - 40)
        y = CENTRO[1] + math.sin(angulo_texto) * (RADIO - 40)
        texto = fuente.render(str(numeros[i]), True, BLANCO)
        VENTANA.blit(texto, (x - texto.get_width() // 2, y - texto.get_height() // 2))

    # Dibujar el marcador
    pygame.draw.polygon(
        VENTANA,
        BLANCO,
        [(CENTRO[0], CENTRO[1] - RADIO - 10), (CENTRO[0] - 10, CENTRO[1] - RADIO - 30), (CENTRO[0] + 10, CENTRO[1] - RADIO - 30)],
    )

# Animación de la ruleta
def ruleta():
    angulo = 0
    velocidad = random.uniform(5, 10)
    desaceleracion = 0.02

    while velocidad > 0:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        angulo += velocidad
        velocidad -= desaceleracion

        dibujar_ruleta(angulo % 360)
        pygame.display.flip()
        pygame.time.delay(30)

    ganador = (int(NUMEROS - (angulo % 360) / (360 / NUMEROS))) % NUMEROS
    return ganador

# Juego principal
def main():
    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    ganador = ruleta()
                    print(f"¡El número ganador es: {ganador}!")

        VENTANA.fill(NEGRO)
        mensaje = fuente.render("Presiona ESPACIO para girar la ruleta", True, BLANCO)
        VENTANA.blit(mensaje, (ANCHO // 2 - mensaje.get_width() // 2, ALTO // 2))
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
