import pygame
pygame.init()
from Jugadores import posiciones_circulo
#JUEGO
screen = pygame.display.set_mode((1800, 900))
clock = pygame.time.Clock()

#COLORES
WHITE          = (255, 255, 255)
BLACK          = (0  , 0  , 0  )
RED            = (255, 0  , 0  )
DARK_RED       = (150, 0  , 0  )
MID_DARK_RED   = (185, 0  , 0  )
GREEN          = (0  , 230, 0  )
DARK_GREEN     = (45 , 87 , 44 )
BROWN          = (135, 80 , 20 )
GOLDEN         = (239, 184, 16 )
GRAY           = (100, 100, 100)
ORANGE         = (255, 165, 0  )
LILAC          = (216, 145, 239)
BLUE           = (0  , 70 , 255)
DARK_ORANGE    = (200, 110, 0  )
DARK_LILAC     = (188, 67 , 226)
DARK_BLUE      = (0  , 0  , 200)

#FUENTES DE TEXTO
arial150 = pygame.font.SysFont("Arial", 150, True)
arial55  = pygame.font.SysFont("Arial", 55       )
arial45  = pygame.font.SysFont("Arial", 45       )
arial40  = pygame.font.SysFont("Arial", 40       )
arial35  = pygame.font.SysFont("Arial", 35       )
arial30  = pygame.font.SysFont("Arial", 30 , True)
arial25  = pygame.font.SysFont("Arial", 25 , True)
arial20  = pygame.font.SysFont("Arial", 20 , True)
arial20b = pygame.font.SysFont("Arial", 20       )
arial18  = pygame.font.SysFont("Arial", 18 , True)
arial15  = pygame.font.SysFont("Arial", 18 , True)
arial15b = pygame.font.SysFont("Arial", 15       )
arial10  = pygame.font.SysFont("Arial", 10 , True)



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

#JUGADORES
jugadores = {
    "0": {
        "jugador":"Naranja", 
        "saldo":{"total":100,"100":0,"50":0,"20":0,"10":0,"5":0}, 
        "color":{"1":ORANGE,"2":DARK_ORANGE}
    },
    "1": {
        "jugador":"Lila",
        "saldo":{"total":100,"100":0,"50":0,"20":0,"10":0,"5":0}, 
        "color":{"1":LILAC,"2":DARK_LILAC}
    },
    "2": {
        "jugador":"Azul", 
        "saldo":{"total":100,"100":0,"50":0,"20":0,"10":0,"5":0}, 
        "color":{"1":BLUE,"2":DARK_BLUE}
    },
    "3": {
        "jugador":"Banca",
        "saldo":{"total":0,"100":0,"50":0,"20":0,"10":0,"5":0}, 
        "color":{"1":DARK_GREEN,"2":WHITE}
    }
}

#!!!!sonido_ruleta = pygame.mixer.Sound('gambling.wav')!!!!

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
boton_x_ruleta = 500
boton_y_ruleta = 500
boton_radio_ruleta = 50
ganador = ""

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

#RATON
mouse = { 
    "x": -1, 
    "y": -1,
    "pressed": False
}

#HISTORIAL
turno = 0
turno_jug = 0
historial = []
#SCROLL
scroll = {
    "percentage": 0,
    "dragging": False,
    "x": 625,
    "y": 400,
    "width": 5,
    "height": 150,
    "radius": 10,
    "surface_offset": 0,
    "visible_height": 540
}
#BOTON
mostrar_historial = False
boton_historial = {
    "x": 40,
    "y": 700,
    "width": 520,
    "height": 150,
}
#SUPERFICIE
y_hist = 540
surface = pygame.Surface((520,y_hist), pygame.SRCALPHA)

teclado = {"pressed": False}

#FICHA
#NARANJA
pos_fichas_naranja = posiciones_circulo((725,730),60,5)
pos_fichas_naranja100 = {
    "x": pos_fichas_naranja[0][0],
    "y": pos_fichas_naranja[0][1]
}
arrastrando_ficha_naranja100 = False
pos_fichas_naranja50 = {
    "x": pos_fichas_naranja[1][0],
    "y": pos_fichas_naranja[1][1]
}
arrastrando_ficha_naranja50 = False
pos_fichas_naranja20 = {
    "x": pos_fichas_naranja[2][0],
    "y": pos_fichas_naranja[2][1]
}
arrastrando_ficha_naranja20 = False
pos_fichas_naranja10 = {
    "x": pos_fichas_naranja[3][0],
    "y": pos_fichas_naranja[3][1]
}
arrastrando_ficha_naranja10 = False
pos_fichas_naranja5 = {
    "x": pos_fichas_naranja[4][0],
    "y": pos_fichas_naranja[4][1]
}
arrastrando_ficha_naranja5 = False
#LILA
pos_fichas_lila = posiciones_circulo((1025,730),60,5)
pos_fichas_lila100 = {
    "x": pos_fichas_lila[0][0],
    "y": pos_fichas_lila[0][1]
}
arrastrando_ficha_lila100 = False
pos_fichas_lila50 = {
    "x": pos_fichas_lila[1][0],
    "y": pos_fichas_lila[1][1]
}
arrastrando_ficha_lila50 = False
pos_fichas_lila20 = {
    "x": pos_fichas_lila[2][0],
    "y": pos_fichas_lila[2][1]
}
arrastrando_ficha_lila20 = False
pos_fichas_lila10 = {
    "x": pos_fichas_lila[3][0],
    "y": pos_fichas_lila[3][1]
}
arrastrando_ficha_lila10 = False
pos_fichas_lila5 = {
    "x": pos_fichas_lila[4][0],
    "y": pos_fichas_lila[4][1]
}
arrastrando_ficha_lila5 = False
#AZUL
pos_fichas_azul = posiciones_circulo((1325,730),60,5)
pos_fichas_azul100 = {
    "x": pos_fichas_azul[0][0],
    "y": pos_fichas_azul[0][1]
}
arrastrando_ficha_azul100 = False
pos_fichas_azul50 = {
    "x": pos_fichas_azul[1][0],
    "y": pos_fichas_azul[1][1]
}
arrastrando_ficha_azul50 = False
pos_fichas_azul20 = {
    "x": pos_fichas_azul[2][0],
    "y": pos_fichas_azul[2][1]
}
arrastrando_ficha_azul20 = False
pos_fichas_azul10 = {
    "x": pos_fichas_azul[3][0],
    "y": pos_fichas_azul[3][1]
}
arrastrando_ficha_azul10 = False
pos_fichas_azul5 = {
    "x": pos_fichas_azul[4][0],
    "y": pos_fichas_azul[4][1]
}
arrastrando_ficha_azul5 = False

centros_tablero = []
pos_y = 50
for i in range(4):
    pos_x = 710
    for i in range(14):
        centros_tablero.append((pos_x,pos_y))
        pos_x += 80
    pos_y += 100
pos_y = 450
for i in range(2):
    pos_x = 710
    for i in range(4):
        centros_tablero.append((pos_x,pos_y))
    pos_y += 100