import model.Dado as Dado
import model.Figura as Figura
import controller.FiguraController as FiguraController
import random as random
class DadoController:
    def __init__(self,escenarioId):
        self.model = Dado.Dado(escenarioId)
        self.inicializar_figuras()
        self.lanzar_dado()

    def inicializar_figuras(self):
        for i in range(3):
            figuraController = FiguraController.FiguraController()
            self.model.figuras.append(figuraController.model)

    def lanzar_dado(self):
        self.model.id = random.randint(1,6)
        if self.model.escenarioId == 1:
            if self.model.id == 1:
                self.model.figuras[0].set_matriz(1)
                self.model.figuras[1].set_matriz(2)
                self.model.figuras[2].set_matriz(3)
            if self.model.id == 2:
                self.model.figuras[0].set_matriz(4)
                self.model.figuras[1].set_matriz(7)
                self.model.figuras[2].set_matriz(8)
            if self.model.id == 3:
                self.model.figuras[0].set_matriz(6)
                self.model.figuras[1].set_matriz(2)
                self.model.figuras[2].set_matriz(4)
            if self.model.id == 4:
                self.model.figuras[0].set_matriz(1)
                self.model.figuras[1].set_matriz(2)
                self.model.figuras[2].set_matriz(3)
            if self.model.id == 5:
                self.model.figuras[0].set_matriz(4)
                self.model.figuras[1].set_matriz(3)
                self.model.figuras[2].set_matriz(2)
            if self.model.id == 6:
                self.model.figuras[0].set_matriz(4)
                self.model.figuras[1].set_matriz(7)
                self.model.figuras[2].set_matriz(8)
        if self.model.escenarioId == 2:
            if self.model.id == 1:
                self.model.figuras[0].set_matriz(8)
                self.model.figuras[1].set_matriz(6)
                self.model.figuras[2].set_matriz(2)
            if self.model.id == 2:
                self.model.figuras[0].set_matriz(9)
                self.model.figuras[1].set_matriz(6)
                self.model.figuras[2].set_matriz(7)
            if self.model.id == 3:
                self.model.figuras[0].set_matriz(4)
                self.model.figuras[1].set_matriz(7)
                self.model.figuras[2].set_matriz(8)
            if self.model.id == 4:
                self.model.figuras[0].set_matriz(8)
                self.model.figuras[1].set_matriz(6)
                self.model.figuras[2].set_matriz(2)
            if self.model.id == 5:
                self.model.figuras[0].set_matriz(6)
                self.model.figuras[1].set_matriz(2)
                self.model.figuras[2].set_matriz(4)
            if self.model.id == 6:
                self.model.figuras[0].set_matriz(4)
                self.model.figuras[1].set_matriz(7)
                self.model.figuras[2].set_matriz(8)
