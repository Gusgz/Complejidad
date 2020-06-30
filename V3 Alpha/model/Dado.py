import model.Figura as Figura
import random as random
class Dado:
    def __init__(self):
        pass

    def lanzar(self,escenarioId,figuras):
        #id = random.randint(1,6)
        id = 1
        if escenarioId == 1:
            if id == 1:
                aux = [1,2,3]
                for i in range(3):
                    figuras[i].generar(aux[i])
            if id == 2:
                aux = [4,7,8]
                for i in range(3):
                    figuras[i].generar(aux[i])
            if id == 3:
                aux = [6,2,4]
                for i in range(3):
                    figuras[i].generar(aux[i])
            if id == 4:
                aux = [1,2,3]
                for i in range(3):
                    figuras[i].generar(aux[i])
            if id == 5:
                aux = [4,3,2]
                for i in range(3):
                    figuras[i].generar(aux[i])
            if id == 6:
                aux = [4,7,8]
                for i in range(3):
                    figuras[i].generar(aux[i])
        if escenarioId == 2:
            if id == 1:
                aux = [8,6,2]
                for i in range(3):
                    figuras[i].generar(aux[i])
            if id == 2:
                aux = [9,6,7]
                for i in range(3):
                    figuras[i].generar(aux[i])
            if id == 3:
                aux = [4,7,8]
                for i in range(3):
                    figuras[i].generar(aux[i])
            if id == 4:
                aux = [8,6,2]
                for i in range(3):
                    figuras[i].generar(aux[i])
            if id == 5:
                aux = [6,2,4]
                for i in range(3):
                    figuras[i].generar(aux[i])
            if id == 6:
                aux = [4,7,8]
                for i in range(3):
                    figuras[i].generar(aux[i])
    