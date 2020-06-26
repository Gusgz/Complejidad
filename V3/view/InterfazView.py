import tkinter as tkinter
class InterfazView:
    def __init__(self,model):
        self.model = model

    def dibujar_figura(self,f,c,matriz,libre,ocupado):
        canvas = tkinter.Canvas(self.model.root,width=90,height=90)
        for i in range(3):
            x = i*30
            for j in range(3):
                y = j*30
                if matriz[j][i] == 0:
                    canvas.create_rectangle(x,y,x+30,y+30,fill=libre)
                if matriz[j][i] == 1:
                    canvas.create_rectangle(x,y,x+30,y+30,fill=ocupado)
        canvas.grid(row=f,column=c)
    
    def dibujar_escenario(self,f,c,matriz,libre,ocupado):
        canvas = tkinter.Canvas(self.model.root,width=120,height=120)
        for i in range(4):
            x = i*30
            for j in range(4):
                y = j*30
                if matriz[j][i] == 0:
                    canvas.create_rectangle(x,y,x+30,y+30,fill=libre)
                if matriz[j][i] == 1:
                    canvas.create_rectangle(x,y,x+30,y+30,fill=ocupado)
        canvas.grid(row=f,column=c,rowspan=3,columnspan=3)

