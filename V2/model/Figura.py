class Figura:

    def __init__(self,filas,columnas,valor_vacio,valor_ocupado):
        self.filas = filas
        self.columnas = columnas
        self.valor_vacio = valor_vacio
        self.valor_ocupado = valor_ocupado
        self.matriz = [[self.valor_vacio]*self.filas for i in range(self.columnas)]
    
    def get_matriz(self):
        return self.matriz

