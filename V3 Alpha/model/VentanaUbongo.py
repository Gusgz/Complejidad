import tkinter as tkinter
class VentanaUbongo:
    def __init__(self,root,tablero):
        self.root = root
        self.tablero = tablero
    
    def iniciar(self):
        self.root.mainloop()

    def finalizar(self):
        self.root.destroy()

    def dibujar_tablero(self):
        canvas = tkinter.Canvas(self.root,width=180,height=90)
        k = 0
        for i in range(3):
            y = i*30
            for j in range(6):
                x = j*30
                canvas.create_oval(x,y,x+30,y+30, width=1, fill=self.tablero.grafo.colores[k])
                k += 1
        canvas.grid(row=0,column=0)


    def dibujar_jugadores(self):
        jugadores = ['A','B','C','D']
        pos = [2,1,4,2]
        for i in range(len(jugadores)):
            lblNombre = tkinter.Label(self.root)
            lblNombre["text"] = jugadores[i] + " " + str(pos[i])
            lblNombre.grid(row=i+1,column=0)

