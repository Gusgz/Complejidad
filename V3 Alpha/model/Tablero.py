import model.Gema as Gema
import model.Grafo as Grafo
import random as random
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
        return lista


                