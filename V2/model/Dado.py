class Dado:
    
    def __init__(self,cantidad,figuras,filas,columnas):
        self.cantidad = cantidad
        self.figuras = figuras
        self.filas = filas
        self.columnas = columnas
        self.matriz = [[" "]*self.filas for i in range(self.columnas)]
    