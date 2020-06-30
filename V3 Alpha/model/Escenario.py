import random as random
class Escenario:
    def __init__(self):
        self.matriz = [[0]*4 for i in range(4)]
        self.cache = []

    def generar(self):
        id = random.randint(1,2)
        if id == 1:
            self.matriz = [
                [1,0,0,0],
                [1,0,0,0],
                [0,0,0,0],
                [1,1,0,0]
            ]
        if id == 2:
            self.matriz = [
                [0,0,0,1],
                [0,0,0,0],
                [0,0,0,0],
                [0,1,1,1]
            ]
        return id
    
    def insertar_figura(self,x,y,figura):
        m = [[0]*4 for i in range(4)]
        for f in range(x,x+3):
            for c in range(y,y+3):
                if f>= 0 and f <=3 and c >=0 and c <= 3:
                    if figura.matriz[c-y][f-x] == 1:
                        self.matriz[c][f] = 1
                        m[c][f] = 1
        return m, figura.color
    
    def esta_completo(self):
        for i in range(3):
            for j in range(3):
                if self.matriz[j][i] == 0:
                    return False
        return True

    def se_puede_insertar_figura(self,x,y,figura):
        cont = 0
        for f in range(x,x+3):
            for c in range(y,y+3):
                if f>= 0 and f <=3 and c >=0 and c <= 3:
                    if figura.matriz[c-y][f-x] == 1 and self.matriz[c][f] == 0 and cont <= figura.bloques:
                        cont += 1
        if cont == figura.bloques:
            return True
        return False

    def se_puede_insertar_prim_coord(self,figura):
        if figura.matriz[0][0] == 1 and self.matriz[0][0] == 0:
            return True
        return False
