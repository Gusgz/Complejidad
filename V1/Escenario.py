class Escenario:
    def __init__(self):
        self.filas = 4
        self.columnas = 4
        self.caracter_vacio = " "
        self.caracter_ocupado = "█"
        self.matriz = [[" "]*self.filas for i in range(self.columnas)]
    
    def generar_escenario(self,codigo):
        if codigo == 1:
            pass
        
    def modificar_coordenada(self,x,y,caracter):
        if self.matriz[x][y] == self.caracter_vacio:
            self.matriz[x][y] = caracter
    
    def visualizar_escenario(self):
        cadena = "__________________\n"
        cadena += "ESCENARIO DE JUEGO\n"
        cadena += "╔═══════════╗\n"
        cadena += "║    X X X X║\n"
        cadena += "║    0 1 2 3║\n"
        for f in range(4):
            cadena += "║Y " + str(f) + "║"
            for c in range(4):
                cadena += str(self.matriz[c][f]) + "║"
            cadena += "\n"
        cadena += "╚═══════════╝\n"
        cadena += "__________________\n"
        print(cadena)

    def insertar_caracter(self,x,y,caracter):
        self.matriz[x][y] = caracter

    def insertar_figura(self,x,y,figura):
        m = figura.get_matriz()
        for f in range(x,x+2):
            for c in range(y,y+2):
                self.matriz[c][f] = m[c-y][f-x]