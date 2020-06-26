import model.Gemas as g
import model.Grafo as gra
import random as random
class TableroController:
    def __init__(self,filas,columnas):
        self.grafo = gra.Grafo()
        self.filas = filas
        self.columnas = columnas

    def generar_gemas(self,colores):
        id_gema = 0
        for i in range(self.filas):
            lista = colores[:]
            for j in range(self.columnas):
                color = random.choice(lista)
                gema = g.Gema(id_gema,color)
                self.grafo.agregar_vertice(gema)
                lista.remove(color)
                id_gema += 1

    def inicio(self,i,div):
        if i != div-1:
            sig = i + 1
            self.grafo.agregar_arista(i,sig,1,True)
            self.grafo.agregar_arista(i,sig+div,1,True)
            self.grafo.agregar_arista(i,sig+(div*2),1,True)
    def medio(self,i,div):
        if i != div-1:
            sig = i + 1
            self.grafo.agregar_arista(i,sig-div,1,True)
            self.grafo.agregar_arista(i,sig,1,True)
            self.grafo.agregar_arista(i,sig+div,1,True)
    def final(self,i,div):
        if i != div-1:
            sig = i + 1
            self.grafo.agregar_arista(i,sig-(div*2),1,True)
            self.grafo.agregar_arista(i,sig-div,1,True)
            self.grafo.agregar_arista(i,sig,1,True)

    def generar_conexiones(self):
        div = len(self.grafo.vertices)//self.filas
        for i in range(self.filas):
            for j in range(self.columnas):
                if j == 0:
                    self.inicio(i+j,div)
                if j > 0 and j < self.columnas - 1:
                    self.medio(div*(i-1)+j-1,div)
                if j == self.columnas-1:
                    self.final(div*(i-1)+j-1,div)