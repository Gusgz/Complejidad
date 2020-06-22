import random as r
import Tarjeta as tarj
class Jugador:
    def __init__(self):
        self.position = -1
        self.name = "empty"
        self.points = 0
        self.tarjeta = tarj.Tarjeta()
    def set_position(self,position):
        self.position = position
    # EL JUGADOR LANZA UN DADO
    def lanzar_dado(dado):
        return r.choice(dado)
    # --------------------
    # MOSTRAR TARJETA
    def _mostrar_tarjeta(self):
        self.tarjeta._imprimir_matriz()
    # --------------------




