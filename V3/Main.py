import model.Figura as Figura
import model.Interfaz as Interfaz
import model.Dado as Dado
import model.Escenario as Escenario
import controller.FiguraController as FiguraController
import controller.InterfazController as InterfazController
import controller.DadoController as DadoController
import controller.EscenarioController as EscenarioController

def fase_escenario():
    escenario = Escenario.Escenario(1)
    escenarioController = EscenarioController.EscenarioController(escenario)
    escenarioController.generar_escenario()
    return escenarioController.model

def fase_dado(escenarioId):
    dado = Dado.Dado(escenarioId)
    dadoController = DadoController.DadoController(dado)
    dadoController.lanzar_dado()
    return dadoController.model.figuras

def fase_interfaz():
    # interfaz
    interfaz = Interfaz.Interfaz()
    interfazController = InterfazController.InterfazController(interfaz)
    interfazController.ajustar_pantalla(800,500)
    # interfaz - escenario
    escenario = fase_escenario()
    interfazController.view.dibujar_escenario(1,0,escenario.matriz,"white","#C0C0C0")
    # interfaz - lanzar dados
    figuras = fase_dado(1)
    # interfaz - dibujar figuras
    interfazController.view.dibujar_figura(0,0,figuras[0].model.matriz,"white",figuras[0].model.color)
    interfazController.view.dibujar_figura(0,1,figuras[1].model.matriz,"white",figuras[1].model.color)
    interfazController.view.dibujar_figura(0,2,figuras[2].model.matriz,"white",figuras[2].model.color)
    # interfaz - insertar figuras
    
    interfazController.run()
    # ___


def run():
    fase_interfaz()

if __name__ == "__main__":
    run()