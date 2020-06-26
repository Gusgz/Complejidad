class Grafo:
    def __init__(self):
        self.vertices = []
        self.matriz = [[0]*0 for i in range(0)]

    def agregar_vertice(self,vertice):
        self.vertices.append(vertice)
        filas = columnas = len(self.vertices)
        matriz_aux = [[0]*filas for i in range(columnas)]
        for f in range(len(self.matriz)):
            for c in range(len(self.matriz)):
                matriz_aux[c][f] = self.matriz[c][f]
        self.matriz = matriz_aux
        return

    def agregar_arista(self,inicio,final,valor,dirigida):
        self.matriz[self.vertices[final].id][self.vertices[inicio].id] = valor
        if not dirigida:
            self.matriz[self.vertices.index(final)][self.vertices.index(inicio)] = valor
        return

    def ver_grafo(self):
        cadena = "\n"
        for i in range(len(self.vertices)):
            cadena += "\t" + str(self.vertices[i].color)
        cadena += "\n"
        for f in range(len(self.matriz)):
            cadena += str(self.vertices[f].color)
            for c in range(len(self.matriz)):
                cadena += "\t" + str(self.matriz[c][f])
            cadena += "\n"
        print(cadena)
        return

    def convertir_lista_adyacencia(self):
        filas = columnas = len(self.vertices)
        lista_adyacencia = [[0]*filas for i in range(columnas)]
        for f in range(len(self.matriz)):
            for c in range(len(self.matriz)):
                if(self.matriz[c][f] > 0):
                    lista_adyacencia[f][c] = self.vertices[c]
        return lista_adyacencia

    def ver_vertices(self):
        cadena = ""
        for i in range(len(self.vertices)):
            cadena += self.vertices[i].color + " "
            if i == 2 or i == 5:
                cadena += "\n"
        print(cadena)