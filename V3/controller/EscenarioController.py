import model.Escenario as Escenario
class EscenarioController:
    def __init__(self):
        self.model = Escenario.Escenario()
    
    def generar_escenario(self):
        if self.model.id == 1:
            self.model.matriz = [
                [1,0,0,0],
                [1,0,0,0],
                [0,0,0,0],
                [1,1,0,0]
            ]
        if self.model.id == 2:
            self.model.matriz = [
                [0,0,0,1],
                [0,0,0,0],
                [0,0,0,0],
                [0,1,1,1]
            ]
    
