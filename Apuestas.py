import Datos as d
import utils
from Jugadores import dibujar_ficha

fichas_naranja = []
fichas_lila = []
fichas_azul = []
fichas_dibujadas = [fichas_naranja, fichas_lila, fichas_azul]
ultima_posicion_mouse = {"x": 0, "y": 0}

def total_apuesta(color):
    valor = 0
    for ficha in fichas_dibujadas[color]:
        valor += int(ficha["valor"])
    return valor

        
def dibujar_ficha_apuestas():
    #NARANJA
    if d.turno_jug == 0:
        #100
        if d.mouse["pressed"] and utils.is_point_in_circle(d.mouse,d.pos_fichas_naranja100,22) and not d.arrastrando_ficha_naranja100 and not d.arrastrando_ficha_naranja50 and not d.arrastrando_ficha_naranja20 and not d.arrastrando_ficha_naranja10 and not d.arrastrando_ficha_naranja5 and d.jugadores["0"]["saldo"]["100"] >= 1:
            d.arrastrando_ficha_naranja100 = True
        if not d.mouse["pressed"]:
            punto = (ultima_posicion_mouse["x"], ultima_posicion_mouse["y"])
            if d.arrastrando_ficha_naranja100 and (utils.is_point_in_polygon(punto, d.puntos_tablero) or utils.is_point_in_polygon(punto, d.puntos_0)) and punto not in d.centros_tablero:
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
            if d.arrastrando_ficha_naranja50 and (utils.is_point_in_polygon(punto, d.puntos_tablero) or utils.is_point_in_polygon(punto, d.puntos_0)) and punto not in d.centros_tablero:
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
            if d.arrastrando_ficha_naranja20 and (utils.is_point_in_polygon(punto, d.puntos_tablero) or utils.is_point_in_polygon(punto, d.puntos_0)) and punto not in d.centros_tablero:
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
            if d.arrastrando_ficha_naranja10 and (utils.is_point_in_polygon(punto, d.puntos_tablero) or utils.is_point_in_polygon(punto, d.puntos_0)) and punto not in d.centros_tablero:
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
            if d.arrastrando_ficha_naranja5 and (utils.is_point_in_polygon(punto, d.puntos_tablero) or utils.is_point_in_polygon(punto, d.puntos_0)) and punto not in d.centros_tablero:
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
            if d.arrastrando_ficha_lila100 and (utils.is_point_in_polygon(punto, d.puntos_tablero) or utils.is_point_in_polygon(punto, d.puntos_0)) and punto not in d.centros_tablero:
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
            if d.arrastrando_ficha_lila50 and (utils.is_point_in_polygon(punto, d.puntos_tablero) or utils.is_point_in_polygon(punto, d.puntos_0)) and punto not in d.centros_tablero:
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
            if d.arrastrando_ficha_lila20 and (utils.is_point_in_polygon(punto, d.puntos_tablero) or utils.is_point_in_polygon(punto, d.puntos_0)) and punto not in d.centros_tablero:
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
            if d.arrastrando_ficha_lila10 and (utils.is_point_in_polygon(punto, d.puntos_tablero) or utils.is_point_in_polygon(punto, d.puntos_0)) and punto not in d.centros_tablero:
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
            if d.arrastrando_ficha_lila5 and (utils.is_point_in_polygon(punto, d.puntos_tablero) or utils.is_point_in_polygon(punto, d.puntos_0)) and punto not in d.centros_tablero:
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
            if d.arrastrando_ficha_azul100 and (utils.is_point_in_polygon(punto, d.puntos_tablero) or utils.is_point_in_polygon(punto, d.puntos_0)) and punto not in d.centros_tablero:
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
            if d.arrastrando_ficha_azul50 and (utils.is_point_in_polygon(punto, d.puntos_tablero) or utils.is_point_in_polygon(punto, d.puntos_0)) and punto not in d.centros_tablero:
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
            if d.arrastrando_ficha_azul20 and (utils.is_point_in_polygon(punto, d.puntos_tablero) or utils.is_point_in_polygon(punto, d.puntos_0)) and punto not in d.centros_tablero:
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
            if d.arrastrando_ficha_azul10 and (utils.is_point_in_polygon(punto, d.puntos_tablero) or utils.is_point_in_polygon(punto, d.puntos_0)) and punto not in d.centros_tablero:
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
            if d.arrastrando_ficha_azul5 and (utils.is_point_in_polygon(punto, d.puntos_tablero) or utils.is_point_in_polygon(punto, d.puntos_0)) and punto not in d.centros_tablero:
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

def calculos_apuestas(ganador):
    for i in range(0,len(fichas_dibujadas)):
        for i2 in range(0, len(fichas_dibujadas[i])):
            #0
            if utils.is_point_in_polygon((fichas_dibujadas[i][i2]["x"],fichas_dibujadas[i][i2]["y"]), d.puntos_0):
                if ganador == 0:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #1
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":710,"y":250,"width":80,"height":100}):
                if ganador == 1:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #2
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":710,"y":150,"width":80,"height":100}):
                if ganador == 2:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #3
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":710,"y":50,"width":80,"height":100}):
                if ganador == 3:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #4
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":790,"y":250,"width":80,"height":100}):
                if ganador == 4:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #5
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":790,"y":150,"width":80,"height":100}):
                if ganador == 5:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #6
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":790,"y":50,"width":80,"height":100}):
                if ganador == 6:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #7
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":870,"y":250,"width":80,"height":100}):
                if ganador == 7:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #8
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":870,"y":150,"width":80,"height":100}):
                if ganador == 8:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #9
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":870,"y":50,"width":80,"height":100}):
                if ganador == 9:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #10
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":950,"y":250,"width":80,"height":100}):
                if ganador == 10:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #11
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":950,"y":150,"width":80,"height":100}):
                if ganador == 11:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #12
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":950,"y":50,"width":80,"height":100}):
                if ganador == 12:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #13
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1030,"y":250,"width":80,"height":100}):
                if ganador == 13:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #14
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1030,"y":150,"width":80,"height":100}):
                if ganador == 14:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #15
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1030,"y":50,"width":80,"height":100}):
                if ganador == 15:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #16 
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1110,"y":250,"width":80,"height":100}):
                if ganador == 16:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #17
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1110,"y":150,"width":80,"height":100}):
                if ganador == 17:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #18
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1110,"y":50,"width":80,"height":100}):
                if ganador == 18:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #19
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1190,"y":250,"width":80,"height":100}):
                if ganador == 19:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #20
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1190,"y":150,"width":80,"height":100}):
                if ganador == 20:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #21
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1190,"y":50,"width":80,"height":100}):
                if ganador == 21:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #22
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1270,"y":250,"width":80,"height":100}):
                if ganador == 22:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #23
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1270,"y":150,"width":80,"height":100}):
                if ganador == 23:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #24
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1270,"y":50,"width":80,"height":100}):
                if ganador == 24:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #25
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1350,"y":250,"width":80,"height":100}):
                if ganador == 25:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #26
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1350,"y":150,"width":80,"height":100}):
                if ganador == 26:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #27
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1350,"y":50,"width":80,"height":100}):
                if ganador == 27:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #28
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1430,"y":250,"width":80,"height":100}):
                if ganador == 28:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #29
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1430,"y":150,"width":80,"height":100}):
                if ganador == 29:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #30
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1430,"y":50,"width":80,"height":100}):
                if ganador == 30:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #31
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1510,"y":250,"width":80,"height":100}):
                if ganador == 31:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #32
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1510,"y":150,"width":80,"height":100}):
                if ganador == 32:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #33
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1510,"y":50,"width":80,"height":100}):
                if ganador == 33:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #34
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1590,"y":250,"width":80,"height":100}):
                if ganador == 34:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #35
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1590,"y":150,"width":80,"height":100}):
                if ganador == 35:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #36
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1590,"y":50,"width":80,"height":100}):
                if ganador == 36:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #1º 12
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":710,"y":350,"width":320,"height":100}):
                if ganador == 1 or ganador == 2 or ganador == 3 or ganador == 4 or ganador == 5 or ganador == 6 or ganador == 7 or ganador == 8 or ganador == 9 or ganador == 10 or ganador == 11 or ganador == 12:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 2
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #2º 12
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1030,"y":350,"width":320,"height":100}):
                if ganador == 13 or ganador == 14 or ganador == 15 or ganador == 16 or ganador == 17 or ganador == 18 or ganador == 19 or ganador == 20 or ganador == 21 or ganador == 22 or ganador == 23 or ganador == 24:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 2
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #3º 12
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1350,"y":350,"width":320,"height":100}):
                if ganador == 25 or ganador == 26 or ganador == 27 or ganador == 28 or ganador == 29 or ganador == 30 or ganador == 31 or ganador == 32 or ganador == 33 or ganador == 34 or ganador == 35 or ganador == 36:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 2
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #1º 2to1
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1670,"y":250,"width":80,"height":100}):
                if ganador == 1 or ganador == 4 or ganador == 7 or ganador == 10 or ganador == 13 or ganador == 16 or ganador == 19 or ganador == 22 or ganador == 25 or ganador == 28 or ganador == 31 or ganador == 34:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 2
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #2º 2to1
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1670,"y":150,"width":80,"height":100}):
                if ganador == 2 or ganador == 5 or ganador == 8 or ganador == 11 or ganador == 14 or ganador == 17 or ganador == 20 or ganador == 23 or ganador == 26 or ganador == 29 or ganador == 32 or ganador == 35:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 2
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #3º 2to1
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1670,"y":50,"width":80,"height":100}):
                if ganador == 3 or ganador == 6 or ganador == 9 or ganador == 12 or ganador == 15 or ganador == 18 or ganador == 21 or ganador == 24 or ganador == 27 or ganador == 30 or ganador == 33 or ganador == 36:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 2
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #1to18
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":710,"y":450,"width":160,"height":100}):
                if ganador == 1 or ganador == 2 or ganador == 3 or ganador == 4 or ganador == 5 or ganador == 6 or ganador == 7 or ganador == 8 or ganador == 9 or ganador == 10 or ganador == 11 or ganador == 12 or ganador == 13 or ganador == 14 or ganador == 15 or ganador == 16 or ganador == 17 or ganador == 18:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #Par
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":870,"y":450,"width":160,"height":100}):
                if ganador == 2 or ganador == 4 or ganador == 6 or ganador == 8 or ganador == 10 or ganador == 12 or ganador == 14 or ganador == 16 or ganador == 18 or ganador == 20 or ganador == 22 or ganador == 24 or ganador == 26 or ganador == 28 or ganador == 30 or ganador == 32 or ganador == 34 or ganador == 36:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #Rojo
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1030,"y":450,"width":160,"height":100}):
                if ganador == 1 or ganador == 3 or ganador == 5 or ganador == 7 or ganador == 9 or ganador == 12 or ganador == 14 or ganador == 16 or ganador == 18 or ganador == 19 or ganador == 21 or ganador == 23 or ganador == 25 or ganador == 27 or ganador == 30 or ganador == 32 or ganador == 34 or ganador == 36:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #Negro
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1190,"y":450,"width":160,"height":100}):
                if ganador == 2 or ganador == 4 or ganador == 6 or ganador == 8 or ganador == 10 or ganador == 11 or ganador == 13 or ganador == 15 or ganador == 17 or ganador == 20 or ganador == 22 or ganador == 24 or ganador == 26 or ganador == 28 or ganador == 29 or ganador == 31 or ganador == 33 or ganador == 35:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #Impar
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1350,"y":450,"width":160,"height":100}):
                if ganador == 1 or ganador == 3 or ganador == 5 or ganador == 7 or ganador == 9 or ganador == 11 or ganador == 13 or ganador == 15 or ganador == 17 or ganador == 19 or ganador == 21 or ganador == 23 or ganador == 25 or ganador == 27 or ganador == 29 or ganador == 31 or ganador == 33 or ganador == 35:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
            #19to36
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1510,"y":450,"width":160,"height":100}):
                if ganador == 19 or ganador == 20 or ganador == 21 or ganador == 22 or ganador == 23 or ganador == 24 or ganador == 25 or ganador == 26 or ganador == 27 or ganador == 28 or ganador == 29 or ganador == 30 or ganador == 31 or ganador == 32 or ganador == 33 or ganador == 34 or ganador == 35 or ganador == 36:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])
                else:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] -= int(fichas_dibujadas [i][i2]["valor"])
                            d.jugadores["3"]["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"])