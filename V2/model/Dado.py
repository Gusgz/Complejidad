class Dado:
    
    def __init__(self,n,filas,columnas,valor_vacio,valor_ocupado):
        self.figuras = []
        self.n = n
        self.filas = filas
        self.columnas = columnas
        self.valor_vacio = valor_vacio
        self.valor_ocupado = valor_ocupado
        self.matriz = [[self.valor_vacio]*self.filas for i in range(self.columnas)]
    