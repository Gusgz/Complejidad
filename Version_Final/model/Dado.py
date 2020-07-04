import random as rand
class Dado:
    def __init__(self,escenario,figuras):
        self.escenario = escenario
        self.figuras = figuras
        pass

    def lanzar(self):
        # GENERA EL ESCENARIO
        #self.escenario.id = rand.randint(1,2)
        self.escenario.id = 1
        self.escenario.generar()
        # GENERA LAS FIGURAS POR ESCENARIO
        #id = rand.randint(1,6)
        id = 1
        #id = 3 no
        #id = 1
        if self.escenario.id == 1:
            if id == 1:
                aux = [1,2,3]
                for i in range(3):
                    self.figuras[i].generar(aux[i])
            if id == 2:
                aux = [7,4,8]
                for i in range(3):
                    self.figuras[i].generar(aux[i])
            if id == 3:
                aux = [2,6,4]
                for i in range(3):
                    self.figuras[i].generar(aux[i])
            if id == 4:
                aux = [1,2,3]
                for i in range(3):
                    self.figuras[i].generar(aux[i])
            if id == 5:
                aux = [2,4,3]
                for i in range(3):
                    self.figuras[i].generar(aux[i])
            if id == 6:
                aux = [7,4,8]
                for i in range(3):
                    self.figuras[i].generar(aux[i])
        if self.escenario.id == 2:
            if id == 1:
                aux = [8,6,2]
                for i in range(3):
                    self.figuras[i].generar(aux[i])
            if id == 2:
                aux = [9,6,7]
                for i in range(3):
                    self.figuras[i].generar(aux[i])
            if id == 3:
                aux = [4,7,8]
                for i in range(3):
                    self.figuras[i].generar(aux[i])
            if id == 4:
                aux = [8,6,2]
                for i in range(3):
                    self.figuras[i].generar(aux[i])
            if id == 5:
                aux = [2,6,4]
                for i in range(3):
                    self.figuras[i].generar(aux[i])
            if id == 6:
                aux = [4,7,8]
                for i in range(3):
                    self.figuras[i].generar(aux[i])
    