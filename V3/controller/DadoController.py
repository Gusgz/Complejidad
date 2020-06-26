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
        self.model.id = 1
        self.model.escenarioId = 1
        #self.id = random.randint(1,6)
        if self.model.escenarioId == 1:
            if self.model.id == 1:
                self.model.figuras[0].generar(1)
                self.model.figuras[1].generar(2)
                self.model.figuras[2].generar(3)
            if self.model.id == 2:
                # AYUDA AQUI AMIGO
                # FIJATE DE LA PLANTILLA DE UBONGO
                # HAY 2 MODELOS DE TARJETAS
                # ESTE DE AQUI ES PARA EL MODELO 1
                # AL LANZAR EL DADO SE VA A GENERAR UN ID 
                # PARA CADA ID SE VA A GENERAR LAS FIGURAS DE LA PLANTILLA 1
                # EL ID DEL DADO VA DE 1 A 6
                pass
            if self.model.id == 3:
                pass
            if self.model.id == 4:
                pass
            if self.model.id == 5:
                pass
            if self.model.id == 6:
                pass
            pass
        if self.model.escenarioId == 2:
            if self.model.id == 1:
                pass
            if self.model.id == 2:
                pass
            if self.model.id == 3:
                pass
            if self.model.id == 4:
                pass
            if self.model.id == 5:
                pass
            if self.model.id == 6:
                pass
            pass
    
    def generar_figuras(self):
        pass
