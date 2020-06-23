class Figura:
    def __init__(self):
        # variables para la matriz
        self.filas = 3
        self.columnas = 3
        self.caracter_vacio = " "
        self.caracter_ocupado = "█"
        self.matriz = [[self.caracter_vacio]*self.filas for i in range(self.columnas)]
        # ---
    
    def get_coordenada_x_y(self,x,y):
        return self.matriz[y][x]
    
    def get_matriz(self):
        return self.matriz

    def generar(self,codigo):
        if codigo == 1:
            self.matriz[0][0] = self.caracter_ocupado
            self.matriz[0][1] = self.caracter_ocupado
            self.matriz[0][2] = self.caracter_ocupado
            self.matriz[1][2] = self.caracter_ocupado
            self.matriz[2][2] = self.caracter_ocupado
        if codigo == 2:
            self.matriz[0][0] = self.caracter_ocupado
            self.matriz[1][0] = self.caracter_ocupado
        if codigo == 3:
            self.matriz[1][0] = self.caracter_ocupado
            self.matriz[1][1] = self.caracter_ocupado
