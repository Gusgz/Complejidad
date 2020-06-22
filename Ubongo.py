import Jugador as j
import Grafo as gr
import Computer as c
import random as r
import time as t
from os import system
import sys,traceback
import Tarjeta as tarjeta
import Figura as f
import Dado as dado

tablero = [[""]*6 for i in range(12)]

# --------------------------------------------------
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



# --------------------------------------------------
# MENU PARA EL JUEGO
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
# OPCIÓN NUEVO JUGADOR
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
# AGREGAR COMPUTADOR
def _computador_agregar():
    cadena = "COMPUTADOR AGREGAR\n"
    cadena += "--------------------\n"
    nombre = input("NOMBRE: ")
    cadena += "--------------------\n"
    computador = c.Computer()
    computador.name = nombre
    return computador
# OPCIÓN VER JUGADORES
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
# --------------------------------------------------



# --------------------------------------------------
# FASE INGRESO DE DATOS
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

# FASE EMPEZAR JUEGO
def _fase_empezar_juego(jugadores):
    turnos = 6
    for i in range(turnos):
        print("JUEGO # "+str(i+1))
        # computadora lanza un dado
        # cada jugador arma la pieza según la figura mostrada
        for jugador in jugadores:
            a = t.perf_counter()
            print("EL JUGADOR "+jugador.name+" TIENE 3 OPCIONES PARA ARMAR EL JUEGO")
            jugador._mostrar_tarjeta()
            while a <= 30 :
                
                print(str(int(a))+" segundos...")
                system("cls")
        # según vayan acabando, se establece un orden de prioridad con diferentes beneficios

# FASE RESULTADO DE DATOS
def _fase_resultado_datos():
# --------------------------------------------------

    pass

# --------------------------------------------------
# UBONGO
def _ubongo():
    # FASE DE INGRESO DE DATOS
    '''jugadores,n = _fase_ingreso_datos()
    cadena = "JUEGO VA A EMPEZAR EN 5 SEGUNDOS ...\n"
    for jugador in jugadores:
        cadena += jugador.name + "\n"
    print(cadena)
    t.sleep(5)
    # --------------------
    # FASE EMPEZAR JUEGO
    _fase_empezar_juego(jugadores)
    # --------------------
    # FASE RESULTADO DE DATOS
    # --------------------'''
    d = dado.Dado()
    d._dibujar_figuras()

    t = tarjeta.Tarjeta()
    t._imprimir_matriz()
# --------------------------------------------------



# --------------------------------------------------
# INICIA LA APLICACIÓN
if __name__ == "__main__":
    _ubongo()
    pass
# --------------------------------------------------