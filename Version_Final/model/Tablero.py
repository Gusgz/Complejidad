import model.Grafo as Grafo
import random as random
import tkinter as tk
class Tablero:
    def __init__(self):
        self.grafo = Grafo.Grafo()

    def generar_gemas(self):
        colores = ['red','blue','yellow','red','blue','yellow']
        for i in range(3):
            x = i*6
            aux = colores[:]
            for j in range(6):
                color = random.choice(aux)
                #gema = Gema.Gema(x+j,color)
                self.grafo.agregar_vertice(x+j,color)
                aux.remove(color)

    def generar_conexiones(self):
        n = len(self.grafo.vertices)
        lista = []
        for i in range(3):
            x = i*6
            for j in range(6):
                aristas = []
                for k in range(3):
                    y = k*6 + 1 + j
                    if x+j != y and x+j != 5 and x+j != 11 and x+j != 17:
                        peso = 2
                        if self.grafo.colores[x+j] == self.grafo.colores[y]:
                            peso = 1
                        self.grafo.agregar_arista(x+j,y,peso)
                        aristas.append((y,peso))
                lista.append(aristas)
        #return lista

    def dibujar(self,win):
        canvas = tk.Canvas(win,width=30*6,height=30*3)
        for i in range(3):
            y = i*30
            k = i*6
            for j in range(6):
                x = j*30
                canvas.create_oval(x,y,x+30,y+30, width=1, fill=self.grafo.colores[k+j])
        canvas.grid(row=0,column=0)
                