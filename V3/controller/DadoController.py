import model.Figura as Figura
import controller.FiguraController as FiguraController
import random as random
class DadoController:
    def __init__(self,model):
        self.model = model
        self.inicializar_figuras()

    def inicializar_figuras(self):
        for i in range(3):
            figura = Figura.Figura()
            figuraController = FiguraController.FiguraController(figura)
            self.model.figuras.append(figuraController)

    def lanzar_dado(self):
        self.model.id = 2
        self.model.escenarioId = 1
        #self.id = random.randint(1,6)
        if self.model.escenarioId == 1:
            #id por cara de dado
            if self.model.id == 1:
                self.model.figuras[0].generar(1)
                self.model.figuras[1].generar(2)
                self.model.figuras[2].generar(3)
            if self.model.id == 2:
                self.model.figuras[0].generar(3)
                self.model.figuras[1].generar(4)
                self.model.figuras[2].generar(5)
            if self.model.id == 3:
                self.model.figuras[0].generar(6)
                self.model.figuras[1].generar(2)
                self.model.figuras[2].generar(4)
            if self.model.id == 4:
                self.model.figuras[0].generar(4)
                self.model.figuras[1].generar(7)
                self.model.figuras[2].generar(8)
            if self.model.id == 5:
                self.model.figuras[0].generar(4)
                self.model.figuras[1].generar(3)
                self.model.figuras[2].generar(2)
            if self.model.id == 6:
                self.model.figuras[0].generar(3)
                self.model.figuras[1].generar(4)
                self.model.figuras[2].generar(5)
              
        if self.model.escenarioId == 2:
            if self.model.id == 1:
                self.model.figuras[0].generar(5)
                self.model.figuras[1].generar(4)
                self.model.figuras[2].generar(3)
            if self.model.id == 2:
                self.model.figuras[0].generar(9)
                self.model.figuras[1].generar(6)
                self.model.figuras[2].generar(7)
            if self.model.id == 3:
                self.model.figuras[0].generar(6)
                self.model.figuras[1].generar(5)
                self.model.figuras[2].generar(4)
            if self.model.id == 4:
                self.model.figuras[0].generar(8)
                self.model.figuras[1].generar(6)
                self.model.figuras[2].generar(2)
            if self.model.id == 5:
                self.model.figuras[0].generar(6)
                self.model.figuras[1].generar(2)
                self.model.figuras[2].generar(4)
            if self.model.id == 6:
                self.model.figuras[0].generar(4)
                self.model.figuras[1].generar(7)
                self.model.figuras[2].generar(8)

    
    def generar_figuras(self):
        pass
