class EscenarioView:
    def __init__(self,escenario):
        self.model = escenario
    
    def visualizar_escenario(self):
        cadena = ""
        cadena += "╔═══════════════╗\n"
        cadena += "║    0 1 2 3 4 5║\n"
        cadena += "║   ╔═╦═╦═╦═╦═╦═╣\n"
        for f in range(self.model.filas):
            cadena += "║ " + str(f) + " ║"
            for c in range(self.model.columnas):
                cadena += str(self.model.matriz[c][f]) + "║"
            cadena += "\n"
        cadena += "╚═══╩═╩═╩═╩═╩═╩═╝\n"
        print(cadena)