class JugadorView:
    def __init__(self,jugador):
        self.model = jugador
    def visualizar(self):
        cadena = ""
        cadena += "╔═════════╗\n"
        cadena += "║JUGADOR  ║\t" + str(self.model.id) + "\n"
        cadena += "║NOMBRE\t  ║\t" + self.model.nombre + "\n"
        cadena += "║POSICION ║\t" + str(self.model.posicion) + "\n"
        cadena += "╚═════════╝\n"
        print(cadena)