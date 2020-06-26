import tkinter as tk
class Interfaz():
    def __init__(self,root):
        self.root = root
    def generar_tablero(self,f,c,matriz,color):
        canvas = tk.Canvas(self.root,width=270,height=270)
        for i in range(6):
            x = i*30
            for j in range(6):
                y = j*30
                if matriz[j][i] == 0:
                    canvas.create_rectangle(x,y,x+30,y+30,fill="#F7F7F7")
                if matriz[j][i] == 1:
                    canvas.create_rectangle(x,y,x+30,y+30,fill="red")
        canvas.grid(row=f,column=c,rowspan=3,columnspan=3)
    def generar_figura(self,f,c,matriz,color):
        canvas = tk.Canvas(self.root,width=90,height=90)
        for i in range(3):
            x = i*30
            for j in range(3):
                y = j*30
                if matriz[j][i] == 0:
                    canvas.create_rectangle(x,y,x+30,y+30,fill="#F7F7F7")
                if matriz[j][i] == 1:
                    canvas.create_rectangle(x,y,x+30,y+30,fill=color)
        canvas.grid(row=f,column=c)


    