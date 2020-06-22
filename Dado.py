import Figura as f
class Dado:
    def __init__(self):
        self.figuras = []
        self.matriz = [[" "]*4 for i in range(8)]
        self._agregar_figuras()
        self._unir_figuras()
    # 
    def _agregar_figuras(self):
        for i in range(3):
            figura = f.Figura()
            figura._generar_figura(i+1)
            self.figuras.append(figura)
    #
    def _unir_figuras(self):
        for f in range(4):
            for c in range(8):
                if c <= 1:
                    self.matriz[c][f] = self.figuras[0]._obtener_figura(c,f)
                if c >= 3 and c <= 4:
                    self.matriz[c][f] = self.figuras[1]._obtener_figura(c-3,f)
                if c >= 6:
                    self.matriz[c][f] = self.figuras[2]._obtener_figura(c-6,f)
    #
    def _dibujar_figuras(self):
        cadena = "\n"
        for f in range(4):
            for c in range(8):
                cadena += self.matriz[c][f]
            cadena += "\n"
        print(cadena)


                


