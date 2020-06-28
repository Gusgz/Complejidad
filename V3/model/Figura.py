class Figura:
    def __init__(self):
        self.color = ""
        self.matriz = [[0]*3 for i in range(3)]
    
    def set_matriz(self,codigo):
        if codigo == 1:
            self.color = "gold"
            self.matriz = [
                [0,0,1],
                [0,1,1],
                [0,0,1]
            ]
        if codigo == 2:
            self.color = "green"
            self.matriz = [
                [0,1,1],
                [0,1,1],
                [0,0,1]
            ]
        if codigo == 3:
            self.color = "light sea green"
            self.matriz = [
                [0,0,0],
                [1,0,0],
                [1,1,0]
            ]
        if codigo == 4:
            self.color = "yellow green"
            self.matriz = [
                [0,1,1],
                [0,0,1],
                [0,0,1]
            ]
        if codigo == 5:
            self.color = "deep pink"
            self.matriz = [
                [0,0,1],
                [0,0,1],
                [0,1,1]
            ]
        if codigo == 6:
            self.color = "blue"
            self.matriz = [
                [0,0,1],
                [0,0,1],
                [0,0,1]
            ]
        if codigo == 7:
            self.color = "royal blue"
            self.matriz = [
                [0,1,0],
                [0,1,1],
                [0,0,1]
            ]
        if codigo == 8:
            self.color = "red"
            self.matriz = [
                [0,0,0],
                [0,1,1],
                [0,1,1]
            ]
        if codigo == 9:
            self.color = "yellow"
            self.matriz = [
                [1,1,0],
                [0,1,0],
                [0,1,1]
            ]

