class FiguraView():
    def __init__(self,figura):
        self.figura = figura
    
    def visualizar(self):
        cadena = "\n"
        for f in range(self.figura.filas):
            for c in range(self.figura.columnas):
                cadena += str(self.figura.matriz[c][f])
            cadena += "\n"
        print(cadena)
