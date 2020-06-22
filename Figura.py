import random as r
class Figura:
    def __init__(self):
        self.filas = 4
        self.columnas = 2
        self.matriz = [[" "]*self.filas for i in range(self.columnas)]
    def _generar_figura(self,n):
        if n == 1:
            self.matriz[0][3] = "█"
            self.matriz[1][0] = "█"
            self.matriz[1][1] = "█"
            self.matriz[1][2] = "█"
            self.matriz[1][3] = "█"
        if n == 2:
            self.matriz[0][1] = "█"
            self.matriz[1][1] = "█"
            self.matriz[1][2] = "█"
            self.matriz[1][3] = "█"
        if n == 3:
            self.matriz[0][1] = "█"
            self.matriz[1][0] = "█"
            self.matriz[1][1] = "█"
            self.matriz[1][2] = "█"
            self.matriz[1][3] = "█"
    def _obtener_figura(self,y,x):
        return self.matriz[y][x]