class Figura:
    def __init__(self):
        self.id = 0
        self.rotacion = 0
        self.invertido = False
        self.bloques = 0
        self.color = ""
        self.matriz = [[0]*3 for i in range(3)]
    
    def generar(self,id):
        self.id = id
        self.rotacion = 0
        self.invertido = False
        if id == 1:
            self.color = "gold"
            self.bloques = 4
            self.matriz = [
                [1,0,0],
                [1,1,0],
                [1,0,0]
            ]
        if id == 2:
            self.color = "green"
            self.bloques = 5
            self.matriz = [
                [1,1,0],
                [1,1,0],
                [1,0,0]
            ]
        if id == 3:
            self.color = "light sea green"
            self.bloques = 3
            self.matriz = [
                [1,1,0],
                [1,0,0],
                [0,0,0]
            ]
        if id == 4:
            self.color = "yellow green"
            self.bloques = 4
            self.matriz = [
                [1,1,0],
                [1,0,0],
                [1,0,0]
            ]
        # SIN USO
        if id == 5:
            self.color = "deep pink"
            self.bloques = 4
            self.matriz = [
                [0,0,1],
                [0,0,1],
                [0,1,1]
            ]
        if id == 6:
            self.color = "blue"
            self.bloques = 3
            self.matriz = [
                [1,0,0],
                [1,0,0],
                [1,0,0]
            ]
        if id == 7:
            self.color = "royal blue"
            self.bloques = 4
            self.matriz = [
                [1,0,0],
                [1,1,0],
                [0,1,0]
            ]
        if id == 8:
            self.color = "red"
            self.bloques = 4
            self.matriz = [
                [1,1,0],
                [1,1,0],
                [0,0,0]
            ]
        if id == 9:
            self.color = "yellow"
            self.bloques = 5
            self.matriz = [
                [1,1,0],
                [0,1,0],
                [0,1,1]
            ]

    def rotar(self):
        m = []
        for f in range(len(self.matriz[0])):
            m.append([])
            for c in range(len(self.matriz)):
                m[f].append(self.matriz[len(self.matriz)-1-c][f])
        self.matriz = m
        self.rotacion += 1
        if self.rotacion == 4:
            self.rotacion = 0

    def invertir(self):
        self.matriz = list(reversed(self.matriz))
        self.invertido = not self.invertido

