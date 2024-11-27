import Datos as d
import utils
from Jugadores import dibujar_ficha


def dibujar_ficha_apuestas():
    #NARANJA
    if d.turno_jug == 0:
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_naranja100,22):
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"100",d.jugadores["0"]["color"]["1"],d.jugadores["0"]["color"]["2"])
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_naranja50,22):
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"50",d.jugadores["0"]["color"]["1"],d.jugadores["0"]["color"]["2"])
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_naranja20,22):
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"20",d.jugadores["0"]["color"]["1"],d.jugadores["0"]["color"]["2"])    
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_naranja10,22):
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"10",d.jugadores["0"]["color"]["1"],d.jugadores["0"]["color"]["2"])
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_naranja5,22):
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"5",d.jugadores["0"]["color"]["1"],d.jugadores["0"]["color"]["2"])
    #LILA
    if d.turno_jug == 1:
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_lila100,22):
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"100",d.jugadores["1"]["color"]["1"],d.jugadores["1"]["color"]["2"])
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_lila50,22):
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"50",d.jugadores["1"]["color"]["1"],d.jugadores["1"]["color"]["2"])
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_lila20,22):
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"20",d.jugadores["1"]["color"]["1"],d.jugadores["1"]["color"]["2"])       
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_lila10,22):
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"10",d.jugadores["1"]["color"]["1"],d.jugadores["1"]["color"]["2"])
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_lila5,22):
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"5",d.jugadores["1"]["color"]["1"],d.jugadores["1"]["color"]["2"])
    #AZUL
    if d.turno_jug == 2:
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_azul100,22):
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"100",d.jugadores["2"]["color"]["1"],d.jugadores["2"]["color"]["2"])
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_azul50,22):
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"50",d.jugadores["2"]["color"]["1"],d.jugadores["2"]["color"]["2"])
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_azul20,22):
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"20",d.jugadores["2"]["color"]["1"],d.jugadores["2"]["color"]["2"])      
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_azul10,22):
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"10",d.jugadores["2"]["color"]["1"],d.jugadores["2"]["color"]["2"])
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_azul5,22):
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"5",d.jugadores["2"]["color"]["1"],d.jugadores["2"]["color"]["2"])