import view.EscenarioView as ev
class EscenarioController:
    def __init__(self,escenario):
        self.model = escenario
        self.view = ev.EscenarioView(escenario)
    
    def generar_escenario(self,codigo):
        if codigo == 1:
            pass
