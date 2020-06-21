import Jugador as j
import Grafo as gr
import Computer as comp
import random as r
import time as t
from os import system

tablero = [[""]*6 for i in range(12)]

# GENERA UNA GEMA ALEATORIAMENTE Y LA GUARDA EN EL TABLERO
def generar_gemas(tablero):
    colores = ["ROJO","AZUL","VERD","AMAR","MORA","NARA"]
    for columna in range(12):
        aux = colores[:]
        for fila in range(6):
            color = r.choice(aux)
            tablero[columna][fila] = color
            aux.remove(color)
# --------------------------------------------------

# DIBUJA EL TABLERO DE UBONGO EN LA CONSOLA
def imprimir_tablero():
    global tablero
    cadena = "\n"
    for f in range(6):
        for c in range(12):
            cadena += "\t" + tablero[c][f]
        cadena += "\n"
    print(cadena)
# --------------------------------------------------
'''
def init():
    generar_gemas()
    imprimir_tablero()
    n = 0
    name = ""
    while n<=0 or n>=4:
        n = int(input("¿Cuántos jugadores van a participar? MAX 3\n"))
    for i in range(n):
        print("_____ JUGADOR " + str(i+1) + " _____")
        name = str(input("nombre: "))
        p = pl.Jugador()
        p.name = name
        lp.append(p)
    c = comp.Computer()
    lp.append(c)

def game():
    global lp
    aux = lp[:]
    cont = 0
    while len(aux)>0:
        w = r.choice(aux)
        print(w.name + " ha ganado en el puesto " + str(cont+1))
        aux.remove(w)
        cont+=1
        
def application():
    init()
    for i in range(6):
        print("_____ JUEGO "+str(i+1)+" _____")
        game()
        t.sleep(3)'''

def _menu(n):
    cadena = "--------------------\n"
    cadena += "1) NUEVO JUGADOR\n"
    cadena += "2) AGREGAR COMPUTADOR\n"
    cadena += "3) VER JUGADORES\n"
    cadena += "5) SALIR\n"
    cadena += "--------------------\n"
    cadena += "JUGADORES: "+str(n)+"/4\n"
    print(cadena)
    pass

def _jugador_agregar(nombre,posicion):
    jugador = j.Jugador()
    jugador.name = nombre
    jugador.position = posicion
    return jugador

def _ver_jugadores(jugadores):
    cadena = ""
    n = 0
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
    opcion = 0
    while opcion >= 1 or n <= 4:
        _menu(n)
        opcion = int(input("OPCIÓN:"))
        system("cls")
        if opcion == 1:
            cadena = "JUGADOR AGREGAR\n"
            cadena += "--------------------\n"
            nombre = input("NOMBRE: ")
            posicion = int(input("POSICIÓN: "))
            cadena += "--------------------\n"
            jugadores.append(_jugador_agregar(nombre,posicion))
            n += 1
        if opcion == 3:
            _ver_jugadores(jugadores)
        system("cls")

def _ubongo():
    # FASE DE INGRESO DE DATOS
    _fase_ingreso_datos()
    # --------------------
    # REALIZA LOS 6 TURNOS DEL JUEGO
    for i in range(6):
        print("juego #"+str(i+1))
        pass
    # --------------------
    # OBTIENE RESULTADOS
    # --------------------
    # VISUALIZA LOS GANADORES
    # --------------------
    pass

# INICIA LA APLICACIÓN
if __name__ == "__main__":
    _ubongo()
    pass
# --------------------------------------------------