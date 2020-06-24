# FIGURAS
import model.Figura as f
import controller.FiguraController as fc
# DADO
import model.Dado as d
import controller.DadoController as dc
# ESCENARIO
import model.Escenario as e
import controller.EscenarioController as ec
# JUGADOR
import model.Jugador as j
import controller.JugadorController as jc
# OTROS
from os import system
from os import sys
import time as time
import random as random

def menu(n):
    cadena =  "╔═╦════════════════════╗\n"
    cadena += "║1║ Agregar jugador    ║\n"
    cadena += "║2║ Agregar bot        ║\n"
    cadena += "║3║ Ver participantes  ║\n"
    cadena += "╠═╬════════════════════╣\n"
    cadena += "║8║ Jugar          "+str(n)+"/4 ║\n"
    cadena += "╠═╬════════════════════╣\n"
    cadena += "║9║ Salir              ║\n"
    cadena += "╚═╩════════════════════╝\n"
    print(cadena)

def fase_datos():
    participantes = []
    nombres_bot = ["Alpha","Bravo","Charlie"]
    n = 0
    opcion = 0
    while n < 4:
        system("cls")
        menu(n)
        opcion = int(input("OPCION: "))
        if opcion == 1:
            # Agregar jugador
            n += 1
            nombre = input("NOMBRE: ")
            posicion = int(input("POSICION: "))
            jug_model = j.Jugador(nombre,posicion)
            participantes.append(jug_model)
        if opcion == 2:
            # Agregar bot
            n += 1
            jug_model = j.Jugador(n,random.choice(nombres_bot),random.randint(1,4))
            nombres_bot.remove(jug_model.nombre)
            participantes.append(jug_model)
        if opcion == 3:
            # Ver participantes
            for i in range(n):
                jug_ctlr = jc.JugadorController(participantes[i])
                jug_ctlr.view.visualizar()
            time.sleep(5)
        if opcion == 9:
            sys.exit()
    return participantes

def fase_juego(participantes):
    # SE GENERAN 3 FIGURAS
    figuras = []
    n = 0
    for i in range(3):
        fig_model = f.Figura(3,3,"×","█")
        fig_ctlr = fc.FiguraController(fig_model)
        fig_ctlr.generar(i+1)
        figuras.append(fig_model)
        n += 1
    # SE CREA EL DADO QUE VA A SER LANZADO Y GENERA LAS 3 FIGURAS
    dado_model = d.Dado(n,figuras,3,9)
    dado_ctlr = dc.DadoController(dado_model)
    dado_ctlr.view.visualizar_figuras()
    # SE CREA EL ESCENARIO QUE EL JUGADOR VA A INTERACTUAR CON ESTE
    esc_model = e.Escenario(6,6,"█","×")
    esc_ctlr = ec.EscenarioController(esc_model)
    esc_ctlr.generar_escenario(1)
    esc_ctlr.view.visualizar_escenario()
    # INSERCCIÓN 1
    x = int(input("X: "))
    y = int(input("Y: "))
    esc_ctlr.insertar_figura(x,y,dado_ctlr.dado.figuras[0])
    esc_ctlr.view.visualizar_escenario()
    # INSERCCIÓN 2
    x = int(input("X: "))
    y = int(input("Y: "))
    esc_ctlr.insertar_figura(x,y,dado_ctlr.dado.figuras[1])
    esc_ctlr.view.visualizar_escenario()
    # INSERCCIÓN 3
    x = int(input("X: "))
    y = int(input("Y: "))
    esc_ctlr.insertar_figura(x,y,dado_ctlr.dado.figuras[2])
    esc_ctlr.view.visualizar_escenario()

if __name__ == "__main__":
    participantes = fase_datos()
    fase_juego(participantes)