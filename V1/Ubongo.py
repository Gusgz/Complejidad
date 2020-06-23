import Jugador as j
import Grafo as gr
import Computer as c
import random as r
import time as t
from os import system
import sys,traceback
import Escenario as esc
import Figura as figura
import Dado as dad
import threading
#
import tkinter as tk
import Util as Util
from Interfaz import *

tablero = [[""]*6 for i in range(12)]

def generar_gemas(tablero):
    colores = ["ROJO","AZUL","VERD","AMAR","MORA","NARA"]
    for columna in range(12):
        aux = colores[:]
        for fila in range(6):
            color = r.choice(aux)
            tablero[columna][fila] = color
            aux.remove(color)

def imprimir_tablero():
    global tablero
    cadena = "\n"
    for f in range(6):
        for c in range(12):
            cadena += "\t" + tablero[c][f]
        cadena += "\n"
    print(cadena)

def _menu(n):
    cadena = "--------------------\n"
    cadena += "1) NUEVO JUGADOR\n"
    cadena += "2) AGREGAR COMPUTADOR\n"
    cadena += "3) VER JUGADORES\n"
    cadena += "4) !EMPREZAR!\n"
    cadena += "5) SALIR\n"
    cadena += "--------------------\n"
    cadena += "JUGADORES: "+str(n)+"/4\n"
    print(cadena)

def _jugador_agregar():
    cadena = "JUGADOR AGREGAR\n"
    cadena += "--------------------\n"
    nombre = input("NOMBRE: ")
    posicion = int(input("POSICIÓN: "))
    cadena += "--------------------\n"
    jugador = j.Jugador()
    jugador.name = nombre
    jugador.position = posicion
    return jugador

def _computador_agregar():
    cadena = "COMPUTADOR AGREGAR\n"
    cadena += "--------------------\n"
    nombre = input("NOMBRE: ")
    cadena += "--------------------\n"
    computador = c.Computer()
    computador.name = nombre
    return computador

def _ver_jugadores(jugadores):
    cadena = ""
    n = 1
    for jugador in jugadores:
        cadena += "--------------------\n"
        cadena += "JUGADOR # " + str(n) + "\n"
        cadena += "NOMBRE: " + jugador.name + "\n"
        cadena += "POSICIÓN: " + str(jugador.position) + "\n"
        cadena += "--------------------\n"
        n += 1
    cadena += "... 3 segundos"
    print(cadena)
    t.sleep(3)

def _fase_ingreso_datos():
    jugadores = []
    n = 0
    opcion = 1
    while opcion > 0 and n < 4:
        _menu(n)
        opcion = int(input("OPCIÓN:"))
        system("cls")
        if opcion == 1:
            jugadores.append(_jugador_agregar())
            n += 1
        if opcion == 2:
            jugadores.append(_computador_agregar())
            n += 1
        if opcion == 3:
            _ver_jugadores(jugadores)
        if opcion == 4:
            opcion = 0
            if n == 0:
                sys.exit(0)
            if n == 1:
                jugadores.append(_computador_agregar())
                n += 1
        if opcion == 5:
            sys.exit(0)
        system("cls")
    return jugadores,n

def _fase_empezar_juego():
    turnos = 6
    for i in range(1):
        # computadora lanza un dado
        # UN DADO TIENE UNA IMAGEN CON UNA SERIE DE FIGURAS GENERADAS
        dado = dad.Dado()
        dado._lanzar_dado() 
        escenario = esc.Escenario()
        escenario._generar_escenario(1)
        escenario._imprimir_matriz()
        
        '''escenario._update_coordenada(x,y,"H")
        escenario._imprimir_matriz()'''
        # cada jugador arma la pieza según la figura mostrada
        # según vayan acabando, se establece un orden de prioridad con diferentes beneficios

def _fase_resultado_datos():
    pass

def _ubongo():
    # FASE DE INGRESO DE DATOS
    '''jugadores,n = _fase_ingreso_datos()
    cadena = "JUEGO VA A EMPEZAR EN 5 SEGUNDOS ...\n"
    for jugador in jugadores:
        cadena += jugador.name + "\n"
    print(cadena)
    t.sleep(5)
    # --------------------'''
    # FASE EMPEZAR JUEGO
    #_fase_empezar_juego()
    '''# --------------------
    # FASE RESULTADO DE DATOS
    # --------------------'''

def rotar_matriz(matriz):
    m = []
    for f in range(len(matriz[0])):
        m.append([])
        for c in range(len(matriz)):
            m[f].append(matriz[len(matriz)-1-c][f])
    return m

def aqui():
    # dado
    '''dado = dad.Dado()
    dado.lanzar()
    dado.visualizar_figuras()
    m = rotar_matriz(dado.get_figura(0).get_matriz())
    cadena = ""
    for f in range(2):
        for c in range(2):
            cadena += str(m[c][f])
        cadena += "\n"
    ma = rotar_matriz(m)
    cadena2 = ""
    for f in range(2):
        for c in range(2):
            cadena2 += str(ma[c][f])
        cadena2 += "\n"
    print(cadena)
    print(cadena2)'''
    # escenario
    #escenario = esc.Escenario()
    #escenario.generar_escenario(1)
    #escenario.visualizar_escenario()
    #escenario.insertar_figura(0,0,dado.get_figura(0))
    #escenario.visualizar_escenario()
    '''movimientos = 18
    while movimientos != 0:
        system("cls")
        dado.visualizar_figuras()
        escenario.visualizar_escenario()
        print("LE QUEDAN ",movimientos, " MOVIMIENTOS")
        x = int(input("X: "))
        y = int(input("Y: "))
        escenario.insertar_caracter(x,y,"¤")
        movimientos -= 1'''

def oficial_juego():
    fig = figura.Figura()
    fig.generar(1)
    m = fig.get_matriz()
    cadena = ""
    for f in range(fig.filas):
        for c in range(fig.columnas):
            cadena += str(m[c][f])
        cadena += "\n"
    print(cadena)
    r = rotar_matriz(m)
    cadena = ""
    for f in range(len(r[0])):
        for c in range(len(r)):
            cadena += str(r[c][f])
        cadena += "\n"
    print(cadena)
    r2 = rotar_matriz(r)
    cadena = ""
    for f in range(len(r2[0])):
        for c in range(len(r2)):
            cadena += str(r2[c][f])
        cadena += "\n"
    print(cadena)
    r3 = rotar_matriz(r2)
    cadena = ""
    for f in range(len(r3[0])):
        for c in range(len(r3)):
            cadena += str(r3[c][f])
        cadena += "\n"
    print(cadena)
    pass

if __name__ == "__main__":
    oficial_juego()
    pass
