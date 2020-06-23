import model.Dado as dado
import controller.DadoController as dc

def run():
    obj_dado = dado.Dado(3,3,9," ","█")
    dado_ctlr = dc.DadoController(obj_dado)
    dado_ctlr.generar_figuras()
    dado_ctlr.unir_figuras()
    dado_ctlr.view.visualizar_figuras()


if __name__ == "__main__":
    run()
