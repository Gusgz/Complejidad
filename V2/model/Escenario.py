class Escenario:
    def __init__(self,filas,columnas,valor_vacio,valor_ocupado):
        self.filas = filas
        self.columnas = columnas
        self.valor_vacio = valor_vacio
        self.valor_ocupado = valor_ocupado
        self.matriz = [[valor_vacio]*self.filas for i in range(self.columnas)]

    def insertar_figura(self,x,y,figura):
        m = figura.get_matriz()
        for f in range(x,x+2):
            for c in range(y,y+2):
                self.matriz[c][f] = m[c-y][f-x]