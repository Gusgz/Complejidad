import model.Figura as f
import controller.FiguraController as fc
import view.DadoView as dv
class DadoController:

    def __init__(self,dado):
        self.dado = dado
        self.view = dv.DadoView(self.dado)
        self.generar_figuras()
        self.unir_figuras()

    # ESTA FUNCIÓN SE DEBE USAR EN OTRA CLASE GENERAL
    def rotar_matriz(self,matriz):
        m = []
        for f in range(len(matriz[0])):
            m.append([])
            for c in range(len(matriz)):
                m[f].append(matriz[len(matriz)-1-c][f])
        return m

    def generar_figuras(self):
        for i in range(self.dado.n):
            obj_figura = f.Figura(3,3," ","█")
            figura_ctlr = fc.FiguraController(obj_figura)
            figura_ctlr.generar(1)
            self.dado.figuras.append(figura_ctlr.figura)

    def unir_figuras(self):
        div = self.dado.columnas//self.dado.n
        for f in range(self.dado.filas):
            for c in range(self.dado.columnas):
                if c < div:
                    self.dado.matriz[c][f] = self.dado.figuras[0].matriz[c][f]
                if c >= div and c < div*2:
                    self.dado.matriz[c][f] = self.dado.figuras[1].matriz[c-div][f]
                if c >= div*2:
                    self.dado.matriz[c][f] = self.dado.figuras[2].matriz[c-div*2][f]