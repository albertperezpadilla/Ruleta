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
                    print("FUNCIONA 0 OTRO")
            #1
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":710,"y":250,"width":80,"height":100}):
                if ganador == 1:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    print("FUNCIONA 1 OTRO")
            #2
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":710,"y":150,"width":80,"height":100}):
                if ganador == 2:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    print("FUNCIONA 2 OTRO")
            #3
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":710,"y":50,"width":80,"height":100}):
                if ganador == 3:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    print("FUNCIONA 3 OTRO")
            #4
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":790,"y":250,"width":80,"height":100}):
                if ganador == 4:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    print("FUNCIONA 4 OTRO")
            #5
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":790,"y":150,"width":80,"height":100}):
                if ganador == 5:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    print("FUNCIONA 5 OTRO")
            #6
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":790,"y":50,"width":80,"height":100}):
                if ganador == 6:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    print("FUNCIONA 6 OTRO")
            #7
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":870,"y":250,"width":80,"height":100}):
                if ganador == 7:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    print("FUNCIONA 7 OTRO")
            #8
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":870,"y":150,"width":80,"height":100}):
                if ganador == 8:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    print("FUNCIONA 8 OTRO")
            #9
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":870,"y":50,"width":80,"height":100}):
                if ganador == 9:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    print("FUNCIONA 9 OTRO")
            #10
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":950,"y":250,"width":80,"height":100}):
                if ganador == 10:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    print("FUNCIONA 10 OTRO")
            #11
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":950,"y":150,"width":80,"height":100}):
                if ganador == 11:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    print("FUNCIONA 11 OTRO")
            #12
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":950,"y":50,"width":80,"height":100}):
                if ganador == 12:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    print("FUNCIONA 12 OTRO")
            #13
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1030,"y":250,"width":80,"height":100}):
                if ganador == 13:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    print("FUNCIONA 13 OTRO")
            #14
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1030,"y":150,"width":80,"height":100}):
                if ganador == 14:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    print("FUNCIONA 14 OTRO")
            #15
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1030,"y":50,"width":80,"height":100}):
                if ganador == 15:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    print("FUNCIONA 15 OTRO")
            #16 
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1110,"y":250,"width":80,"height":100}):
                if ganador == 16:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    print("FUNCIONA 16 OTRO")
            #17
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1110,"y":150,"width":80,"height":100}):
                if ganador == 17:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    print("FUNCIONA 17 OTRO")
            #18
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1110,"y":50,"width":80,"height":100}):
                if ganador == 18:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    print("FUNCIONA 18 OTRO")
            #19
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1190,"y":250,"width":80,"height":100}):
                if ganador == 19:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    print("FUNCIONA 19 OTRO")
            #20
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1190,"y":150,"width":80,"height":100}):
                if ganador == 20:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    print("FUNCIONA 20 OTRO")
            #21
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1190,"y":50,"width":80,"height":100}):
                if ganador == 21:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    print("FUNCIONA 21 OTRO")
            #22
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1270,"y":250,"width":80,"height":100}):
                if ganador == 22:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    print("FUNCIONA 22 OTRO")
            #23
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1270,"y":150,"width":80,"height":100}):
                if ganador == 23:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    print("FUNCIONA 23 OTRO")
            #24
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1270,"y":50,"width":80,"height":100}):
                if ganador == 24:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    print("FUNCIONA 24 OTRO")
            #25
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1350,"y":250,"width":80,"height":100}):
                if ganador == 25:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    print("FUNCIONA 25 OTRO")
            #26
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1350,"y":150,"width":80,"height":100}):
                if ganador == 26:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    print("FUNCIONA 26 OTRO")
            #27
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1350,"y":50,"width":80,"height":100}):
                if ganador == 27:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    print("FUNCIONA 27 OTRO")
            #28
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1430,"y":250,"width":80,"height":100}):
                if ganador == 28:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    print("FUNCIONA 28 OTRO")
            #29
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1430,"y":150,"width":80,"height":100}):
                if ganador == 29:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    print("FUNCIONA 29 OTRO")
            #30
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1430,"y":50,"width":80,"height":100}):
                if ganador == 30:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    print("FUNCIONA 30 OTRO")
            #31
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1510,"y":250,"width":80,"height":100}):
                if ganador == 31:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    print("FUNCIONA 31 OTRO")
            #32
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1510,"y":150,"width":80,"height":100}):
                if ganador == 32:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    print("FUNCIONA 32 OTRO")
            #33
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1510,"y":50,"width":80,"height":100}):
                if ganador == 33:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    print("FUNCIONA 33 OTRO")
            #34
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1590,"y":250,"width":80,"height":100}):
                if ganador == 34:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    print("FUNCIONA 34 OTRO")
            #35
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1590,"y":150,"width":80,"height":100}):
                if ganador == 35:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    print("FUNCIONA 35 OTRO")
            #36
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1590,"y":50,"width":80,"height":100}):
                if ganador == 36:
                    for clave, jugador in d.jugadores.items():
                        if jugador["color"]["1"] == fichas_dibujadas [i][i2]["color"]:
                            jugador["saldo"]["total"] += int(fichas_dibujadas [i][i2]["valor"]) * 35
                else:
                    print("FUNCIONA 36 OTRO")
            #1º 12
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":710,"y":350,"width":320,"height":100}):
                if ganador == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12:
                    print("FUNCIONA 1º 12")
                else:
                    print("FUNCIONA 1º 12 OTRO")
            #2º 12
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1030,"y":350,"width":320,"height":100}):
                if ganador == 13 or 14 or 15 or 16 or 17 or 18 or 19 or 20 or 21 or 22 or 23 or 24:
                    print("FUNCIONA 2º 12")
                else:
                    print("FUNCIONA 2º 12 OTRO")
            #3º 12
            if utils.is_point_in_rect({"x":fichas_dibujadas[i][i2]["x"],"y":fichas_dibujadas[i][i2]["y"]},{"x":1350,"y":350,"width":320,"height":100}):
                if ganador == 25 or 26 or 27 or 28 or 29 or 30 or 31 or 32 or 33 or 34 or 35 or 36:
                    print("FUNCIONA 3º 12")
                else:
                    print("FUNCIONA 3º 12 OTRO")
            #1º 2to1
            
            #2º 2to1

            #3º 2to1

            #1to18

            #19to36

            #Par

            #Inpar

            #Rojo

            #Negro
