class FiguraController:

    def __init__(self,model):
        self.model = model

    def generar(self,codigo):
        if codigo == 1:
            self.model.color = "gold"
            self.model.matriz = [
                [0,0,1],
                [0,1,1],
                [0,0,1]
            ]
        if codigo == 2:
            self.model.color = "green"
            self.model.matriz = [
                [0,1,1],
                [0,1,1],
                [0,0,1]
            ]
        if codigo == 3:
            self.model.color = "light sea green"
            self.model.matriz = [
                [0,0,0],
                [1,0,0],
                [1,1,0]
            ]
        if codigo == 4:
            self.model.color = "yellow green"
            self.model.matriz = [
                [0,1,1],
                [0,0,1],
                [0,0,1]
            ]
        if codigo == 5:
            self.model.color = "deep pink"
            self.model.matriz = [
                [0,0,1],
                [0,0,1],
                [0,1,1]
            ]
        if codigo == 6:
            self.model.color = "blue"
            self.model.matriz = [
                [0,0,1],
                [0,0,1],
                [0,0,1]
            ]
        if codigo == 7:
            self.model.color = "royal blue"
            self.model.matriz = [
                [0,1,0],
                [0,1,1],
                [0,0,1]
            ]
        if codigo == 8:
            self.model.color = "red"
            self.model.matriz = [
                [0,0,0],
                [0,1,1],
                [0,1,1]
            ]
        if codigo == 9:
            self.model.color = "yellow"
            self.model.matriz = [
                [1,1,0],
                [0,1,0],
                [0,1,1]
            ]
        # SI LEES ESTO ERES GEY