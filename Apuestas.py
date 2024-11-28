import Datos as d
import utils
from Jugadores import dibujar_ficha

fichas_naranja = []
fichas_lila = []
fichas_azul = []
fichas_dibujadas = [fichas_naranja, fichas_lila, fichas_azul]
ultima_posicion_mouse = {"x": 0, "y": 0}

def dibujar_ficha_apuestas():
    #NARANJA
    if d.turno_jug == 0:
        #100
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_naranja100,22) and not d.arrastrando_ficha_naranja100 and not d.arrastrando_ficha_naranja50 and not d.arrastrando_ficha_naranja20 and not d.arrastrando_ficha_naranja10 and not d.arrastrando_ficha_naranja5 and d.jugadores["0"]["saldo"]["100"] >= 1:
            d.arrastrando_ficha_naranja100 = True
        if not d.mouse["pressed"]:
            punto = (ultima_posicion_mouse["x"], ultima_posicion_mouse["y"])
            if d.arrastrando_ficha_naranja100 and (utils.is_point_in_polygon(punto, d.puntos_tablero) or utils.is_point_in_polygon(punto, d.puntos_0)):
                fichas_naranja.append({"x": ultima_posicion_mouse["x"], "y": ultima_posicion_mouse["y"], "valor": "100", "color": d.jugadores["0"]["color"]["1"], "color2": d.jugadores["0"]["color"]["2"],})
                d.jugadores["0"]["saldo"]["100"] -= 1
            d.arrastrando_ficha_naranja100 = False
        if d.arrastrando_ficha_naranja100 == True:
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"100",d.jugadores["0"]["color"]["1"],d.jugadores["0"]["color"]["2"])
            ultima_posicion_mouse["x"] = d.mouse["x"]
            ultima_posicion_mouse["y"] = d.mouse["y"]

        #50
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_naranja50,22) and not d.arrastrando_ficha_naranja100 and not d.arrastrando_ficha_naranja50 and not d.arrastrando_ficha_naranja20 and not d.arrastrando_ficha_naranja10 and not d.arrastrando_ficha_naranja5 and d.jugadores["0"]["saldo"]["50"] >= 1:
            d.arrastrando_ficha_naranja50 = True
        if not d.mouse["pressed"]:
            punto = (ultima_posicion_mouse["x"], ultima_posicion_mouse["y"])
            if d.arrastrando_ficha_naranja50 and (utils.is_point_in_polygon(punto, d.puntos_tablero) or utils.is_point_in_polygon(punto, d.puntos_0)):
                fichas_naranja.append({"x": ultima_posicion_mouse["x"], "y": ultima_posicion_mouse["y"], "valor": "50", "color": d.jugadores["0"]["color"]["1"], "color2": d.jugadores["0"]["color"]["2"],})
                d.jugadores["0"]["saldo"]["50"] -= 1
            d.arrastrando_ficha_naranja50 = False
        if d.arrastrando_ficha_naranja50 == True:
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"50",d.jugadores["0"]["color"]["1"],d.jugadores["0"]["color"]["2"])
            ultima_posicion_mouse["x"] = d.mouse["x"]
            ultima_posicion_mouse["y"] = d.mouse["y"]

        #20
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_naranja20,22) and not d.arrastrando_ficha_naranja100 and not d.arrastrando_ficha_naranja50 and not d.arrastrando_ficha_naranja20 and not d.arrastrando_ficha_naranja10 and not d.arrastrando_ficha_naranja5 and d.jugadores["0"]["saldo"]["20"] >= 1:
            d.arrastrando_ficha_naranja20 = True
        if not d.mouse["pressed"]:
            punto = (ultima_posicion_mouse["x"], ultima_posicion_mouse["y"])
            if d.arrastrando_ficha_naranja20 and (utils.is_point_in_polygon(punto, d.puntos_tablero) or utils.is_point_in_polygon(punto, d.puntos_0)):
                fichas_naranja.append({"x": ultima_posicion_mouse["x"], "y": ultima_posicion_mouse["y"], "valor": "20", "color": d.jugadores["0"]["color"]["1"], "color2": d.jugadores["0"]["color"]["2"],})
                d.jugadores["0"]["saldo"]["20"] -= 1
            d.arrastrando_ficha_naranja20 = False
        if d.arrastrando_ficha_naranja20 == True:
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"20",d.jugadores["0"]["color"]["1"],d.jugadores["0"]["color"]["2"])
            ultima_posicion_mouse["x"] = d.mouse["x"]
            ultima_posicion_mouse["y"] = d.mouse["y"]

        #10
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_naranja10,22) and not d.arrastrando_ficha_naranja100 and not d.arrastrando_ficha_naranja50 and not d.arrastrando_ficha_naranja20 and not d.arrastrando_ficha_naranja10 and not d.arrastrando_ficha_naranja5 and d.jugadores["0"]["saldo"]["10"] >= 1:
            d.arrastrando_ficha_naranja10 = True
        if not d.mouse["pressed"]:
            punto = (ultima_posicion_mouse["x"], ultima_posicion_mouse["y"])
            if d.arrastrando_ficha_naranja10 and (utils.is_point_in_polygon(punto, d.puntos_tablero) or utils.is_point_in_polygon(punto, d.puntos_0)):
                fichas_naranja.append({"x": ultima_posicion_mouse["x"], "y": ultima_posicion_mouse["y"], "valor": "10", "color": d.jugadores["0"]["color"]["1"], "color2": d.jugadores["0"]["color"]["2"],})
                d.jugadores["0"]["saldo"]["10"] -= 1
            d.arrastrando_ficha_naranja10 = False
        if d.arrastrando_ficha_naranja10 == True:
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"10",d.jugadores["0"]["color"]["1"],d.jugadores["0"]["color"]["2"])
            ultima_posicion_mouse["x"] = d.mouse["x"]
            ultima_posicion_mouse["y"] = d.mouse["y"]

        #5
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_naranja5,22) and not d.arrastrando_ficha_naranja100 and not d.arrastrando_ficha_naranja50 and not d.arrastrando_ficha_naranja20 and not d.arrastrando_ficha_naranja10 and not d.arrastrando_ficha_naranja5 and d.jugadores["0"]["saldo"]["5"] >= 1:
            d.arrastrando_ficha_naranja5 = True
        if not d.mouse["pressed"]:
            punto = (ultima_posicion_mouse["x"], ultima_posicion_mouse["y"])
            if d.arrastrando_ficha_naranja5 and (utils.is_point_in_polygon(punto, d.puntos_tablero) or utils.is_point_in_polygon(punto, d.puntos_0)):
                fichas_naranja.append({"x": ultima_posicion_mouse["x"], "y": ultima_posicion_mouse["y"], "valor": "5", "color": d.jugadores["0"]["color"]["1"], "color2": d.jugadores["0"]["color"]["2"],})
                d.jugadores["0"]["saldo"]["5"] -= 1
            d.arrastrando_ficha_naranja5 = False
        if d.arrastrando_ficha_naranja5 == True:
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"5",d.jugadores["0"]["color"]["1"],d.jugadores["0"]["color"]["2"])
            ultima_posicion_mouse["x"] = d.mouse["x"]
            ultima_posicion_mouse["y"] = d.mouse["y"]

    #LILA
    if d.turno_jug == 1:
        #100
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_lila100,22) and not d.arrastrando_ficha_lila100 and not d.arrastrando_ficha_lila50 and not d.arrastrando_ficha_lila20 and not d.arrastrando_ficha_lila10 and not d.arrastrando_ficha_lila5 and d.jugadores["1"]["saldo"]["100"] >= 1:
            d.arrastrando_ficha_lila100 = True
        if not d.mouse["pressed"]:
            punto = (ultima_posicion_mouse["x"], ultima_posicion_mouse["y"])
            if d.arrastrando_ficha_lila100 and (utils.is_point_in_polygon(punto, d.puntos_tablero) or utils.is_point_in_polygon(punto, d.puntos_0)):
                fichas_lila.append({"x": ultima_posicion_mouse["x"], "y": ultima_posicion_mouse["y"], "valor": "100", "color": d.jugadores["1"]["color"]["1"], "color2": d.jugadores["1"]["color"]["2"],})
                d.jugadores["1"]["saldo"]["100"] -= 1
            d.arrastrando_ficha_lila100 = False
        if d.arrastrando_ficha_lila100 == True:
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"100",d.jugadores["1"]["color"]["1"],d.jugadores["1"]["color"]["2"])
            ultima_posicion_mouse["x"] = d.mouse["x"]
            ultima_posicion_mouse["y"] = d.mouse["y"]

        #50
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_lila50,22) and not d.arrastrando_ficha_lila100 and not d.arrastrando_ficha_lila50 and not d.arrastrando_ficha_lila20 and not d.arrastrando_ficha_lila10 and not d.arrastrando_ficha_lila5 and d.jugadores["1"]["saldo"]["50"] >= 1:
            d.arrastrando_ficha_lila50 = True
        if not d.mouse["pressed"]:
            punto = (ultima_posicion_mouse["x"], ultima_posicion_mouse["y"])
            if d.arrastrando_ficha_lila50 and (utils.is_point_in_polygon(punto, d.puntos_tablero) or utils.is_point_in_polygon(punto, d.puntos_0)):
                fichas_lila.append({"x": ultima_posicion_mouse["x"], "y": ultima_posicion_mouse["y"], "valor": "50", "color": d.jugadores["1"]["color"]["1"], "color2": d.jugadores["1"]["color"]["2"],})
                d.jugadores["1"]["saldo"]["50"] -= 1
            d.arrastrando_ficha_lila50 = False
        if d.arrastrando_ficha_lila50 == True:
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"50",d.jugadores["1"]["color"]["1"],d.jugadores["1"]["color"]["2"])
            ultima_posicion_mouse["x"] = d.mouse["x"]
            ultima_posicion_mouse["y"] = d.mouse["y"]

        #20
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_lila20,22) and not d.arrastrando_ficha_lila100 and not d.arrastrando_ficha_lila50 and not d.arrastrando_ficha_lila20 and not d.arrastrando_ficha_lila10 and not d.arrastrando_ficha_lila5 and d.jugadores["1"]["saldo"]["20"] >= 1:
            d.arrastrando_ficha_lila20 = True
        if not d.mouse["pressed"]:
            punto = (ultima_posicion_mouse["x"], ultima_posicion_mouse["y"])
            if d.arrastrando_ficha_lila20 and (utils.is_point_in_polygon(punto, d.puntos_tablero) or utils.is_point_in_polygon(punto, d.puntos_0)):
                fichas_lila.append({"x": ultima_posicion_mouse["x"], "y": ultima_posicion_mouse["y"], "valor": "20", "color": d.jugadores["1"]["color"]["1"], "color2": d.jugadores["1"]["color"]["2"],})
                d.jugadores["1"]["saldo"]["20"] -= 1
            d.arrastrando_ficha_lila20 = False
        if d.arrastrando_ficha_lila20 == True:
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"20",d.jugadores["1"]["color"]["1"],d.jugadores["1"]["color"]["2"])
            ultima_posicion_mouse["x"] = d.mouse["x"]
            ultima_posicion_mouse["y"] = d.mouse["y"]

        #10     
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_lila10,22) and not d.arrastrando_ficha_lila100 and not d.arrastrando_ficha_lila50 and not d.arrastrando_ficha_lila20 and not d.arrastrando_ficha_lila10 and not d.arrastrando_ficha_lila5 and d.jugadores["1"]["saldo"]["10"] >= 1:
            d.arrastrando_ficha_lila10 = True
        if not d.mouse["pressed"]:
            punto = (ultima_posicion_mouse["x"], ultima_posicion_mouse["y"])
            if d.arrastrando_ficha_lila10 and (utils.is_point_in_polygon(punto, d.puntos_tablero) or utils.is_point_in_polygon(punto, d.puntos_0)):
                fichas_lila.append({"x": ultima_posicion_mouse["x"], "y": ultima_posicion_mouse["y"], "valor": "10", "color": d.jugadores["1"]["color"]["1"], "color2": d.jugadores["1"]["color"]["2"],})
                d.jugadores["1"]["saldo"]["10"] -= 1
            d.arrastrando_ficha_lila10 = False
        if d.arrastrando_ficha_lila10 == True:
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"10",d.jugadores["1"]["color"]["1"],d.jugadores["1"]["color"]["2"])
            ultima_posicion_mouse["x"] = d.mouse["x"]
            ultima_posicion_mouse["y"] = d.mouse["y"]

        #5
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_lila5,22) and not d.arrastrando_ficha_lila100 and not d.arrastrando_ficha_lila50 and not d.arrastrando_ficha_lila20 and not d.arrastrando_ficha_lila10 and not d.arrastrando_ficha_lila5 and d.jugadores["1"]["saldo"]["5"] >= 1:
            d.arrastrando_ficha_lila5 = True
        if not d.mouse["pressed"]:
            punto = (ultima_posicion_mouse["x"], ultima_posicion_mouse["y"])
            if d.arrastrando_ficha_lila5 and (utils.is_point_in_polygon(punto, d.puntos_tablero) or utils.is_point_in_polygon(punto, d.puntos_0)):
                fichas_lila.append({"x": ultima_posicion_mouse["x"], "y": ultima_posicion_mouse["y"], "valor": "5", "color": d.jugadores["1"]["color"]["1"], "color2": d.jugadores["1"]["color"]["2"],})
                d.jugadores["1"]["saldo"]["5"] -= 1
            d.arrastrando_ficha_lila5 = False
        if d.arrastrando_ficha_lila5 == True:
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"5",d.jugadores["1"]["color"]["1"],d.jugadores["1"]["color"]["2"])
            ultima_posicion_mouse["x"] = d.mouse["x"]
            ultima_posicion_mouse["y"] = d.mouse["y"]

    #AZUL
    if d.turno_jug == 2:
        #100
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_azul100,22) and not d.arrastrando_ficha_azul100 and not d.arrastrando_ficha_azul50 and not d.arrastrando_ficha_azul20 and not d.arrastrando_ficha_azul10 and not d.arrastrando_ficha_azul5 and d.jugadores["2"]["saldo"]["100"] >= 1:
            d.arrastrando_ficha_azul100 = True
        if not d.mouse["pressed"]:
            punto = (ultima_posicion_mouse["x"], ultima_posicion_mouse["y"])
            if d.arrastrando_ficha_azul100 and (utils.is_point_in_polygon(punto, d.puntos_tablero) or utils.is_point_in_polygon(punto, d.puntos_0)):
                fichas_azul.append({"x": ultima_posicion_mouse["x"], "y": ultima_posicion_mouse["y"], "valor": "100", "color": d.jugadores["2"]["color"]["1"], "color2": d.jugadores["2"]["color"]["2"],})
                d.jugadores["2"]["saldo"]["100"] -= 1
            d.arrastrando_ficha_azul100 = False
        if d.arrastrando_ficha_azul100 == True:
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"100",d.jugadores["2"]["color"]["1"],d.jugadores["2"]["color"]["2"])
            ultima_posicion_mouse["x"] = d.mouse["x"]
            ultima_posicion_mouse["y"] = d.mouse["y"]

        #50
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_azul50,22) and not d.arrastrando_ficha_azul100 and not d.arrastrando_ficha_azul50 and not d.arrastrando_ficha_azul20 and not d.arrastrando_ficha_azul10 and not d.arrastrando_ficha_azul5 and d.jugadores["2"]["saldo"]["50"] >= 1:
            d.arrastrando_ficha_azul50 = True
        if not d.mouse["pressed"]:
            punto = (ultima_posicion_mouse["x"], ultima_posicion_mouse["y"])
            if d.arrastrando_ficha_azul50 and (utils.is_point_in_polygon(punto, d.puntos_tablero) or utils.is_point_in_polygon(punto, d.puntos_0)):
                fichas_azul.append({"x": ultima_posicion_mouse["x"], "y": ultima_posicion_mouse["y"], "valor": "50", "color": d.jugadores["2"]["color"]["1"], "color2": d.jugadores["2"]["color"]["2"],})
                d.jugadores["2"]["saldo"]["50"] -= 1
            d.arrastrando_ficha_azul50 = False
        if d.arrastrando_ficha_azul50 == True:
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"50",d.jugadores["2"]["color"]["1"],d.jugadores["2"]["color"]["2"])
            ultima_posicion_mouse["x"] = d.mouse["x"]
            ultima_posicion_mouse["y"] = d.mouse["y"]

        #20
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_azul20,22) and not d.arrastrando_ficha_azul100 and not d.arrastrando_ficha_azul50 and not d.arrastrando_ficha_azul20 and not d.arrastrando_ficha_azul10 and not d.arrastrando_ficha_azul5 and d.jugadores["2"]["saldo"]["20"] >= 1:
            d.arrastrando_ficha_azul20 = True
        if not d.mouse["pressed"]:
            punto = (ultima_posicion_mouse["x"], ultima_posicion_mouse["y"])
            if d.arrastrando_ficha_azul20 and (utils.is_point_in_polygon(punto, d.puntos_tablero) or utils.is_point_in_polygon(punto, d.puntos_0)):
                fichas_azul.append({"x": ultima_posicion_mouse["x"], "y": ultima_posicion_mouse["y"], "valor": "20", "color": d.jugadores["2"]["color"]["1"], "color2": d.jugadores["2"]["color"]["2"],})
                d.jugadores["2"]["saldo"]["20"] -= 1
            d.arrastrando_ficha_azul20 = False
        if d.arrastrando_ficha_azul20 == True:
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"20",d.jugadores["2"]["color"]["1"],d.jugadores["2"]["color"]["2"])
            ultima_posicion_mouse["x"] = d.mouse["x"]
            ultima_posicion_mouse["y"] = d.mouse["y"]

        #10     
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_azul10,22) and not d.arrastrando_ficha_azul100 and not d.arrastrando_ficha_azul50 and not d.arrastrando_ficha_azul20 and not d.arrastrando_ficha_azul10 and not d.arrastrando_ficha_azul5 and d.jugadores["2"]["saldo"]["10"] >= 1:
            d.arrastrando_ficha_azul10 = True
        if not d.mouse["pressed"]:
            punto = (ultima_posicion_mouse["x"], ultima_posicion_mouse["y"])
            if d.arrastrando_ficha_azul10 and (utils.is_point_in_polygon(punto, d.puntos_tablero) or utils.is_point_in_polygon(punto, d.puntos_0)):
                fichas_azul.append({"x": ultima_posicion_mouse["x"], "y": ultima_posicion_mouse["y"], "valor": "10", "color": d.jugadores["2"]["color"]["1"], "color2": d.jugadores["2"]["color"]["2"],})
                d.jugadores["2"]["saldo"]["10"] -= 1
            d.arrastrando_ficha_azul10 = False
        if d.arrastrando_ficha_azul10 == True:
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"10",d.jugadores["2"]["color"]["1"],d.jugadores["2"]["color"]["2"])
            ultima_posicion_mouse["x"] = d.mouse["x"]
            ultima_posicion_mouse["y"] = d.mouse["y"]
        
        #5
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_azul5,22) and not d.arrastrando_ficha_azul100 and not d.arrastrando_ficha_azul50 and not d.arrastrando_ficha_azul20 and not d.arrastrando_ficha_azul10 and not d.arrastrando_ficha_azul5 and d.jugadores["2"]["saldo"]["5"] >= 1:
            d.arrastrando_ficha_azul5 = True
        if not d.mouse["pressed"]:
            punto = (ultima_posicion_mouse["x"], ultima_posicion_mouse["y"])
            if d.arrastrando_ficha_azul5 and (utils.is_point_in_polygon(punto, d.puntos_tablero) or utils.is_point_in_polygon(punto, d.puntos_0)):
                fichas_azul.append({"x": ultima_posicion_mouse["x"], "y": ultima_posicion_mouse["y"], "valor": "5", "color": d.jugadores["2"]["color"]["1"], "color2": d.jugadores["2"]["color"]["2"],})
                d.jugadores["2"]["saldo"]["5"] -= 1
            d.arrastrando_ficha_azul5 = False
        if d.arrastrando_ficha_azul5 == True:
            dibujar_ficha(d.mouse["x"],d.mouse["y"],"5",d.jugadores["2"]["color"]["1"],d.jugadores["2"]["color"]["2"])
            ultima_posicion_mouse["x"] = d.mouse["x"]
            ultima_posicion_mouse["y"] = d.mouse["y"]

    for lista in fichas_dibujadas:
        for i in lista:
            dibujar_ficha(i["x"], i["y"], i["valor"], i["color"], i["color2"])