import controller.FiguraController as FiguraController
import controller.InterfazController as InterfazController
import controller.DadoController as DadoController
import controller.EscenarioController as EscenarioController

def generar_escenario():
    escenarioController = EscenarioController.EscenarioController()
    escenarioController.generar_escenario()
    return escenarioController.model

def generar_figuras(escenarioId):
    dadoController = DadoController.DadoController(escenarioId)
    return dadoController.model.figuras

def generar_interfaz(escenario,figuras):
    interfazController = InterfazController.InterfazController(escenario,figuras)
    return interfazController

def run():
    escenario = generar_escenario()
    figuras = generar_figuras(escenario.id)
    controlador = generar_interfaz(escenario,figuras)

if __name__ == "__main__":
    run()