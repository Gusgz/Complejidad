class FiguraController:

    def __init__(self,model):
        self.model = model

    def generar(self,codigo):
        if codigo == 1:
            self.model.color = "yellow"
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
            self.model.color = "skyblue"
            self.model.matriz = [
                [0,0,0],
                [1,0,0],
                [1,1,0]
            ]
        # FALTA AGREGAR MÁS FIGURAS, LAS INDIQUÉ POR EL WSP LAS QUE FALTAN