import view.FiguraView as fv
class FiguraController:

    def __init__(self,figura):
        self.figura = figura
        self.figuraView = fv.FiguraView(self.figura)

    def generar(self,codigo):
        if codigo == 1:
            self.figura.matriz[2][0] = self.figura.valor_ocupado
            self.figura.matriz[2][1] = self.figura.valor_ocupado
            self.figura.matriz[2][2] = self.figura.valor_ocupado
            self.figura.matriz[1][1] = self.figura.valor_ocupado
        if codigo == 2:
            self.figura.matriz[2][0] = self.figura.valor_ocupado
            self.figura.matriz[2][1] = self.figura.valor_ocupado
            self.figura.matriz[2][2] = self.figura.valor_ocupado
            self.figura.matriz[1][0] = self.figura.valor_ocupado
            self.figura.matriz[1][1] = self.figura.valor_ocupado
        if codigo == 3:
            self.figura.matriz[0][1] = self.figura.valor_ocupado
            self.figura.matriz[0][2] = self.figura.valor_ocupado
            self.figura.matriz[1][2] = self.figura.valor_ocupado  