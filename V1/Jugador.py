import random as r
import Escenario as esc
class Jugador:
    def __init__(self):
        self.position = -1
        self.name = "empty"
        self.points = 0
        self.escenario = esc.Escenario()
    def set_position(self,position):
        self.position = position
    #
    # MOSTRAR TARJETA
    def _mostrar_tarjeta(self):
        self.escenario._imprimir_matriz()
    # --------------------




