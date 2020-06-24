import view.EscenarioView as ev
class EscenarioController:
    def __init__(self,escenario):
        self.model = escenario
        self.view = ev.EscenarioView(escenario)
    
    def generar_escenario(self,codigo):
        if codigo == 1:
            for i in range(self.model.columnas):
                self.model.matriz[0][i] = self.model.valor_ocupado
                self.model.matriz[1][i] = self.model.valor_ocupado
                self.model.matriz[5][i] = self.model.valor_ocupado
            self.model.matriz[2][0] = self.model.valor_ocupado
            self.model.matriz[2][1] = self.model.valor_ocupado
            self.model.matriz[2][2] = self.model.valor_ocupado
            self.model.matriz[4][3] = self.model.valor_ocupado
            self.model.matriz[4][4] = self.model.valor_ocupado
            self.model.matriz[4][5] = self.model.valor_ocupado

    def insertar_figura(self,y,x,figura):
        if x >= 4 or y >= 4:
            # validar figura
            print("INSERCCIÓN FUERA DE LOS LÍMITES")
            return
        m = figura.matriz
        filas = figura.filas
        columnas = figura.columnas
        valor_ocupado = figura.valor_ocupado
        for f in range(x,x+filas):
            for c in range(y,y+columnas):
                if m[c-y][f-x] == valor_ocupado:
                    self.model.matriz[c][f] = m[c-y][f-x]

    def validar_coordenada(self,x,y):
        pass