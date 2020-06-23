# DADO
import model.Dado as d
import controller.DadoController as dc
# ESCENARIO
import model.Escenario as e
import controller.EscenarioController as ec

def run():
    # SE CREA EL DADO QUE VA A SER LANZADO Y GENERA LAS 3 FIGURAS
    obj_dado = d.Dado(3,3,9," ","█")
    dado_ctlr = dc.DadoController(obj_dado)
    dado_ctlr.view.visualizar_figuras()
    # SE CREA EL ESCENARIO QUE EL JUGADOR VA A INTERACTUAR CON ESTE
    esc_model = e.Escenario(6,6," ","█")
    esc_ctlr = ec.EscenarioController(esc_model)
    esc_ctlr.view.visualizar_escenario()



if __name__ == "__main__":
    run()
