class DadoView:

    def __init__(self,dado):
        self.dado = dado

    def visualizar_figuras(self):
        div = self.dado.columnas//self.dado.n
        cadena = ""
        cadena += "╔═══╦═══╦═══╗\n"
        cadena += "║A  ║B  ║C  ║\n"
        cadena += "╠═══╬═══╬═══╣\n"
        for f in range(self.dado.filas):
            cadena += "║"
            for c in range(self.dado.columnas):
                if c == div or c == div*2:
                    cadena += "║" + self.dado.matriz[c][f] 
                else:
                    cadena += self.dado.matriz[c][f]
                if c == self.dado.columnas - 1:
                    cadena += "║"
            cadena += "\n"
        cadena += "╚═══╩═══╩═══╝\n"
        print(cadena)