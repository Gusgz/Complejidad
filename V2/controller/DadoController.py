import model.Figura as f
import controller.FiguraController as fc
import view.DadoView as dv
class DadoController:

    def __init__(self,dado):
        self.dado = dado
        self.view = dv.DadoView(self.dado)
        self.unir_figuras()

    def unir_figuras(self):
        div = self.dado.columnas//self.dado.cantidad
        for f in range(self.dado.filas):
            for c in range(self.dado.columnas):
                if c < div:
                    self.dado.matriz[c][f] = self.dado.figuras[0].matriz[c][f]
                if c >= div and c < div*2:
                    self.dado.matriz[c][f] = self.dado.figuras[1].matriz[c-div][f]
                if c >= div*2:
                    self.dado.matriz[c][f] = self.dado.figuras[2].matriz[c-div*2][f]