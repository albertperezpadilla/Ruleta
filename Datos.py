import pygame
pygame.init()

#JUEGO
screen = pygame.display.set_mode((1800, 900))
clock = pygame.time.Clock()

#COLORES
WHITE        = (255, 255, 255)
BLACK        = (0  , 0  , 0  )
RED          = (255, 0  , 0  )
GREEN        = (0  , 255, 0  )
BLUE         = (0  , 0  , 255)
PURPLE       = (128, 0  , 128)
ORANGE       = (255, 165, 0  ) 
YELLOW       = (255, 255, 0  )
BROWN        = (135, 80 , 20 )
GOLDEN       = (239, 184, 16 )
DARK_GREEN   = (45 , 87 , 44 )
DARK_GRAY    = (51 , 47 , 44 )
DARK_RED     = (150, 0  , 0  )
MID_DARK_RED = (185, 0  , 0  )
GRAY         = (130, 130, 130)

#FUENTES DE TEXTO
arial55 = pygame.font.SysFont("Arial", 55)
arial40 = pygame.font.SysFont("Arial", 40)
arial35 = pygame.font.SysFont("Arial", 35)
arial18 = pygame.font.SysFont("Arial", 18, True)

#CASILLAS
casillas = {
    "0":  {"num":0,  "color":GREEN,},
    "1":  {"num":1,  "color":RED  , "pos_ini":()},
    "2":  {"num":2,  "color":BLACK, "pos_ini":()},
    "3":  {"num":3,  "color":RED  , "pos_ini":()},
    "4":  {"num":4,  "color":BLACK, "pos_ini":()},
    "5":  {"num":5,  "color":RED  , "pos_ini":()},
    "6":  {"num":6,  "color":BLACK, "pos_ini":()},
    "7":  {"num":7,  "color":RED  , "pos_ini":()},
    "8":  {"num":8,  "color":BLACK, "pos_ini":()},
    "9":  {"num":9,  "color":RED  , "pos_ini":()},
    "10": {"num":10, "color":BLACK, "pos_ini":()},
    "11": {"num":11, "color":BLACK, "pos_ini":()},
    "12": {"num":12, "color":RED  , "pos_ini":()},
    "13": {"num":13, "color":BLACK, "pos_ini":()},
    "14": {"num":14, "color":RED  , "pos_ini":()},
    "15": {"num":15, "color":BLACK, "pos_ini":()},
    "16": {"num":16, "color":RED  , "pos_ini":()},
    "17": {"num":17, "color":BLACK, "pos_ini":()},
    "18": {"num":18, "color":RED  , "pos_ini":()},
    "19": {"num":19, "color":RED  , "pos_ini":()},
    "20": {"num":20, "color":BLACK, "pos_ini":()},
    "21": {"num":21, "color":RED  , "pos_ini":()},
    "22": {"num":22, "color":BLACK, "pos_ini":()},
    "23": {"num":23, "color":RED  , "pos_ini":()},
    "24": {"num":24, "color":BLACK, "pos_ini":()},
    "25": {"num":25, "color":RED  , "pos_ini":()},
    "26": {"num":26, "color":BLACK, "pos_ini":()},
    "27": {"num":27, "color":RED  , "pos_ini":()},
    "28": {"num":28, "color":BLACK, "pos_ini":()},
    "29": {"num":29, "color":BLACK, "pos_ini":()},
    "30": {"num":30, "color":RED  , "pos_ini":()},
    "31": {"num":31, "color":BLACK, "pos_ini":()},
    "32": {"num":32, "color":RED  , "pos_ini":()},
    "33": {"num":33, "color":BLACK, "pos_ini":()},
    "34": {"num":34, "color":RED  , "pos_ini":()},
    "35": {"num":35, "color":BLACK, "pos_ini":()},
    "36": {"num":36, "color":RED  , "pos_ini":()}
}



#RULETA
CENTRO = (300,300)
RADIO = 210
ultimo_angulo = 0
orden_ruleta = [
    "0" , "32", "15", "19", "4", "21" , 
    "2" , "25", "17", "34", "6", "27" ,
    "13", "36", "11", "30", "8", "23" , 
    "10", "5" , "24", "16", "33", "1" , 
    "20", "14", "31", "9" , "22", "18",
    "29", "7" , "28", "12", "35", "3" , 
    "26"
]
NUMEROS = len(orden_ruleta)
boton_x_ruleta = 550
boton_y_ruleta = 500
boton_radio_ruleta = 50

#TABLERO
orden_tablero = [
    [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36],
    [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35],
    [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
]
row_cont = 0
for row in orden_tablero:
    if row_cont == 0:
        pos = [710, 50]
    elif row_cont == 1:
        pos = [710, 150]
    else:
        pos = [710, 250]
    for i in row:
        casillas[str(i)]["pos_ini"] = (pos[0], pos[1])
        pos[0] += 80
    row_cont += 1
puntos_tablero = [(710, 50), (1750, 50), (1750, 350), (1670, 350), (1670, 550), (710, 550)]
puntos_0 = [(710, 50), (630, 50), (600, 200), (630, 350), (710, 350)]