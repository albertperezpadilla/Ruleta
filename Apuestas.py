import Datos as d
import utils
from Jugadores import dibujar_ficha


def dibujar_ficha_apuestas():
    #NARANJA
    if d.turno_jug == 0:
        #100
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_naranja100,22):
            d.arrastrando_ficha_naranja100 = True
        if not d.mouse["pressed"]:
            d.arrastrando_ficha_naranja100 = False
        if d.arrastrando_ficha_naranja100 == True:
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"100",d.jugadores["0"]["color"]["1"],d.jugadores["0"]["color"]["2"])

        #50
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_naranja50,22):
            d.arrastrando_ficha_naranja50 = True
        if not d.mouse["pressed"]:
            d.arrastrando_ficha_naranja50 = False
        if d.arrastrando_ficha_naranja50 == True:
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"50",d.jugadores["0"]["color"]["1"],d.jugadores["0"]["color"]["2"])

        #20
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_naranja20,22):
            d.arrastrando_ficha_naranja20 = True
        if not d.mouse["pressed"]:
            d.arrastrando_ficha_naranja20 = False
        if d.arrastrando_ficha_naranja20 == True:
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"20",d.jugadores["0"]["color"]["1"],d.jugadores["0"]["color"]["2"])

        #10
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_naranja10,22):
            d.arrastrando_ficha_naranja10 = True
        if not d.mouse["pressed"]:
            d.arrastrando_ficha_naranja10 = False
        if d.arrastrando_ficha_naranja10 == True:
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"10",d.jugadores["0"]["color"]["1"],d.jugadores["0"]["color"]["2"])

        #5
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_naranja5,22):
            d.arrastrando_ficha_naranja5 = True
        if not d.mouse["pressed"]:
            d.arrastrando_ficha_naranja5 = False
        if d.arrastrando_ficha_naranja5 == True:
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"5",d.jugadores["0"]["color"]["1"],d.jugadores["0"]["color"]["2"])

    #LILA
    if d.turno_jug == 1:
        #100
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_lila100,22):
            d.arrastrando_ficha_lila100 = True
        if not d.mouse["pressed"]:
            d.arrastrando_ficha_lila100 = False
        if d.arrastrando_ficha_lila100 == True:
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"100",d.jugadores["1"]["color"]["1"],d.jugadores["1"]["color"]["2"])

        #50
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_lila50,22):
            d.arrastrando_ficha_lila50 = True
        if not d.mouse["pressed"]:
            d.arrastrando_ficha_lila50 = False
        if d.arrastrando_ficha_lila50 == True:
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"50",d.jugadores["1"]["color"]["1"],d.jugadores["1"]["color"]["2"])

        #20
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_lila20,22):
            d.arrastrando_ficha_lila20 = True
        if not d.mouse["pressed"]:
            d.arrastrando_ficha_lila20 = False
        if d.arrastrando_ficha_lila20 == True:
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"20",d.jugadores["1"]["color"]["1"],d.jugadores["1"]["color"]["2"])

        #10     
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_lila10,22):
            d.arrastrando_ficha_lila10 = True
        if not d.mouse["pressed"]:
            d.arrastrando_ficha_lila10 = False
        if d.arrastrando_ficha_lila10 == True:
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"10",d.jugadores["1"]["color"]["1"],d.jugadores["1"]["color"]["2"])

        #5
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_lila5,22):
            d.arrastrando_ficha_lila5 = True
        if not d.mouse["pressed"]:
            d.arrastrando_ficha_lila5 = False
        if d.arrastrando_ficha_lila5 == True:
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"5",d.jugadores["1"]["color"]["1"],d.jugadores["1"]["color"]["2"])

    #AZUL
    if d.turno_jug == 2:
        #100
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_azul100,22):
            d.arrastrando_ficha_azul100 = True
        if not d.mouse["pressed"]:
            d.arrastrando_ficha_azul100 = False
        if d.arrastrando_ficha_azul100 == True:
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"100",d.jugadores["2"]["color"]["1"],d.jugadores["2"]["color"]["2"])

        #50
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_azul50,22):
            d.arrastrando_ficha_azul50 = True
        if not d.mouse["pressed"]:
            d.arrastrando_ficha_azul50 = False
        if d.arrastrando_ficha_azul50 == True:
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"50",d.jugadores["2"]["color"]["1"],d.jugadores["2"]["color"]["2"])

        #20
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_azul20,22):
            d.arrastrando_ficha_azul20 = True
        if not d.mouse["pressed"]:
            d.arrastrando_ficha_azul20 = False
        if d.arrastrando_ficha_azul20 == True:
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"20",d.jugadores["2"]["color"]["1"],d.jugadores["2"]["color"]["2"])

        #10     
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_azul10,22):
            d.arrastrando_ficha_azul10 = True
        if not d.mouse["pressed"]:
            d.arrastrando_ficha_azul10 = False
        if d.arrastrando_ficha_azul10 == True:
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"10",d.jugadores["2"]["color"]["1"],d.jugadores["2"]["color"]["2"])

        #5
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_azul5,22):
            d.arrastrando_ficha_azul5 = True
        if not d.mouse["pressed"]:
            d.arrastrando_ficha_azul5 = False
        if d.arrastrando_ficha_azul5 == True:
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"5",d.jugadores["2"]["color"]["1"],d.jugadores["2"]["color"]["2"])