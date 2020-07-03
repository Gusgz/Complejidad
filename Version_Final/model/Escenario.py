import tkinter as tk
import random as random
class Escenario:
    def __init__(self):
        self.id = 0
        self.matriz = [[0]*4 for i in range(4)]

    def generar(self):
        #self.id = random.randint(1,2)
        self.id = 1
        if self.id == 1:
            self.matriz = [
                [1,0,0,0],
                [1,0,0,0],
                [0,0,0,0],
                [1,1,0,0]
            ]
        if self.id == 2:
            self.matriz = [
                [0,0,0,1],
                [0,0,0,0],
                [0,0,0,0],
                [0,1,1,1]
            ]
    
    def generar_id(self):
        if self.id == 1:
            self.matriz = [
                [1,0,0,0],
                [1,0,0,0],
                [0,0,0,0],
                [1,1,0,0]
            ]
        if self.id == 2:
            self.matriz = [
                [0,0,0,1],
                [0,0,0,0],
                [0,0,0,0],
                [0,1,1,1]
            ]
    
    def insertar_figura(self,x,y,figura):
        m = [[0]*4 for i in range(4)]
        for f in range(x,x+3):
            for c in range(y,y+3):
                if f>= 0 and f <=3 and c >=0 and c <= 3:
                    if figura.matriz[c-y][f-x] == 1:
                        self.matriz[c][f] = 1
                        m[c][f] = 1
        return m, figura.color
    
    def esta_completo(self):
        for i in range(4):
            for j in range(4):
                if self.matriz[j][i] == 0:
                    return False
        return True

    def se_puede_insertar_figura(self,x,y,figura):
        cont = 0
        for f in range(x,x+3):
            for c in range(y,y+3):
                if f>= 0 and f <=3 and c >=0 and c <= 3:
                    if figura.matriz[c-y][f-x] == 1 and self.matriz[c][f] == 0 and cont <= figura.bloques:
                        cont += 1
        if cont == figura.bloques:
            return True
        return False

    def se_puede_insertar_prim_coord(self,figura):
        if figura.matriz[0][0] == 1 and self.matriz[0][0] == 0:
            return True
        return False

    def encontrar_prim_coord_vacia(self):
        for i in range(4):
            for j in range(4):
                if self.matriz[j][i] == 0:
                    return i,j
        return 0,0

    def dibujar(self,win):
        canvas = tk.Canvas(win,width=120,height=120)
        for i in range(4):
            x = i*30
            for j in range(4):
                y = j*30
                if self.matriz[j][i] == 0:
                    canvas.create_rectangle(x,y,x+30,y+30,fill="white")
                if self.matriz[j][i] == 1:
                    canvas.create_rectangle(x,y,x+30,y+30,fill="#C0C0C0")
        canvas.grid(row=1,column=0,columnspan=3)


    def dibujar_con_figura(self,win,m,color):
        canvas = tk.Canvas(win,width=120,height=120)
        for i in range(4):
            x = i*30
            for j in range(4):
                y = j*30
                if self.matriz[j][i] == 0:
                    canvas.create_rectangle(x,y,x+30,y+30,fill="white")
                if self.matriz[j][i] == 1:
                    if m[j][i] == 1:
                        canvas.create_rectangle(x,y,x+30,y+30,fill=color)
                    else:
                        canvas.create_rectangle(x,y,x+30,y+30,fill="#C0C0C0")
        canvas.grid(row=1,column=0,columnspan=3)