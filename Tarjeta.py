class Tarjeta:
    def __init__(self):
        self.matriz = [["█"]*4 for i in range(4)]
    def _modificar_matriz(self,x,y):
            self.matriz[y][x] = chr(219)
    def _generar_tarjeta(self,codigo):
        if codigo == 1:
            pass


    def _imprimir_matriz(self):
        cadena = "  1 2 3 4\n"
        for f in range(4):
            cadena += str(f+1) + " "
            for c in range(4):
                cadena += str(self.matriz[c][f]) + " "
            cadena += "\n"
        print(cadena)