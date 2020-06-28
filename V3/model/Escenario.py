import random as random
class Escenario:
    def __init__(self):
        self.id = random.randint(1,2)
        self.matriz = [[0]*4 for i in range(4)]

    def validar(x,y):
        if x<0 or x>3:

            pass
        if y<0 or y>3:
            pass
        return x,y

    def insertar_figura(self,x,y,figura):
        for f in range(x,x+3):
            for c in range(y,y+3):
                if f>= 0 and f <=3 and c >=0 and c <= 3:
                    if figura.matriz[c-y][f-x] == 1:
                        self.matriz[c][f] = 1
    
    def esta_completo(self):
        for i in range(3):
            for j in range(3):
                if self.matriz[j][i] == 0:
                    return False
        return True

    def se_puede_insertar(self,x,y,figura):
        cont = 0
        for i in range(3):
            for j in range(3):
                if figura.matriz[j][i] == 1:
                    cont += 1
        for f in range(x,x+3):
            for c in range(y,y+3):
                if f>= 0 and f <=3 and c >=0 and c <= 3:
                    if figura.matriz[c-y][f-x] == 1 and self.matriz[c][f] == 0 and cont > 0:
                        cont -= 1
        if cont == 0:
            return True
        return False

    def primera_coordenada(self,figura):
        if figura.matriz[0][0] == 1 and self.matriz[0][0] == 0:
            return True
        return False
