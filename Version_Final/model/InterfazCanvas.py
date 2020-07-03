import tkinter as tk
class InterfazCanvas:
    def __init__(self,root):
        self.root = root
    
    def tablero(self,tablero):
        canvas = tk.Canvas(self.root,width=180,height=90)
        for i in range(3):
            y = i*30
            k = i*6
            for j in range(6):
                x = j*30
                canvas.create_oval(x,y,x+30,y+30, width=1, fill=tablero.grafo.colores[k+j])
        canvas.grid(row=0,column=0)

    def figura(self,win,f,c,matriz,color):
        canvas = tk.Canvas(win,width=90,height=90)
        for i in range(3):
            x = i*30
            for j in range(3):
                y = j*30
                if matriz[j][i] == 0:
                    canvas.create_rectangle(x,y,x+30,y+30,fill="white")
                if matriz[j][i] == 1:
                    canvas.create_rectangle(x,y,x+30,y+30,fill=color)
        canvas.grid(row=f,column=c)

    def figuras(self,win,figuras):
        for i in range(3):
            self.figura(win,0,i,figuras[i].matriz,figuras[i].color)

    def escenario(self,win,escenario):
        canvas = tk.Canvas(win,width=120,height=120)
        for i in range(4):
            x = i*30
            for j in range(4):
                y = j*30
                if escenario.matriz[j][i] == 0:
                    canvas.create_rectangle(x,y,x+30,y+30,fill="white")
                if escenario.matriz[j][i] == 1:
                    canvas.create_rectangle(x,y,x+30,y+30,fill="#C0C0C0")
        canvas.grid(row=1,column=0,columnspan=3)

    def escenario_con_figura(self,escenario,figuras,m,color):
        canvas = tkinter.Canvas(self.root,width=120,height=120)
        for i in range(4):
            x = i*30
            for j in range(4):
                y = j*30
                if escenario.matriz[j][i] == 0:
                    canvas.create_rectangle(x,y,x+30,y+30,fill="white")
                if escenario.matriz[j][i] == 1:
                    if m[j][i] == 1:
                        canvas.create_rectangle(x,y,x+30,y+30,fill=color)
                    else:
                        canvas.create_rectangle(x,y,x+30,y+30,fill="#C0C0C0")
        canvas.grid(row=1,column=0,columnspan=3)