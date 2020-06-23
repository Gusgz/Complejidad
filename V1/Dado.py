import Figura as fig
import random as ran
class Dado:
    def __init__(self):
        self.figuras = []
        # variables para la matriz
        self.filas = 2
        self.columnas = 8
        self.caracter_vacio = " "
        self.caracter_ocupado = "█"
        self.matriz = [[self.caracter_vacio]*self.filas for i in range(self.columnas)]
        # ---
    
    def lanzar(self):
        #n = ran.randint(1,6)
        self.generar_figuras(1)
    
    def generar_figuras(self,n):
        if n == 1:
            for i in range(1,4):
                figura = fig.Figura()
                figura.generar(i)
                self.figuras.append(figura)
        self.unir_figuras()

    def unir_figuras(self):
        for f in range(self.filas):
            for c in range(self.columnas):
                if c <= 1:
                    self.matriz[c][f] = self.figuras[0].get_coordenada_x_y(f,c)
                if c >= 3 and c <= 4:
                    self.matriz[c][f] = self.figuras[1].get_coordenada_x_y(f,c-3)
                if c >= 6:
                    self.matriz[c][f] = self.figuras[2].get_coordenada_x_y(f,c-6)
    
    def visualizar_figuras(self):
        cadena = "________\n"
        cadena += "FIGURAS\n"
        cadena += "________\n"
        cadena += "A |B |C\n"
        for f in range(self.filas):
            for c in range(self.columnas):
                if c == 2 or c == 5 or c == 8:
                    cadena += "|"
                else:
                    cadena += self.matriz[c][f]
            cadena += "\n"
        cadena += "________\n"
        print(cadena)
    
    def get_figura(self,pos):
        return self.figuras[pos]


                


