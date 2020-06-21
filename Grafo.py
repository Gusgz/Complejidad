class Grafo:
    def __init__(self):
        self.vertices = []
        self.matriz = [[0]*0 for i in range(0)]
    # AGREGAR VERTICE
    def agregar_vertice(self,vertice):
        if(self.existe_vertice(vertice)):
            return False
        self.vertices.append(vertice)
        filas = columnas = len(self.vertices)
        matriz_aux = [[0]*filas for i in range(columnas)]
        for f in range(len(self.matriz)):
            for c in range(len(self.matriz)):
                matriz_aux[c][f] = self.matriz[c][f]
        self.matriz = matriz_aux
        return
    # AGREGAR ARISTA
    def agregar_arista(self,inicio,final,valor,dirigida):
        if not(self.existe_vertice(inicio)) or not(self.existe_vertice(final)):
            return False
        self.matriz[self.vertices.index(final)][self.vertices.index(inicio)] = valor
        if not dirigida:
            self.matriz[self.vertices.index(final)][self.vertices.index(inicio)] = valor
        return
    # OBTENER VERTICES
    def obtener_vertices(self):
        return self.vertices
    # OBTENER MATRIZ
    def obtener_matriz(self):
        return self.matriz
    # CAMBIAR_MATRIZ
    def cambiar_matriz(self,m):
        for f in range(len(self.matriz)):
            for c in range(len(self.matriz)):
                self.matriz[c][f] = m[f][c]
        return
    # EXISTE VERTICE
    def existe_vertice(self,vertice):
        if(self.vertices.count(vertice) > 0):
            return True
        else:
            return False
    # IMPRIMIR GRAFO
    def imprimir_grafo(self):
        cadena = "\n"
        for i in range(len(self.vertices)):
            cadena += "\t" + str(self.vertices[i])
        cadena += "\n"
        for f in range(len(self.matriz)):
            cadena += str(self.vertices[f])
            for c in range(len(self.matriz)):
                cadena += "\t" + str(self.matriz[c][f])
            cadena += "\n"
        print(cadena)
        return
    # OBTENER LISTA ADYACENCIA
    def obtener_lista_adyacencia(self):
        filas = columnas = len(self.vertices)
        lista_adyacencia = [[0]*filas for i in range(columnas)]
        for f in range(len(self.matriz)):
            for c in range(len(self.matriz)):
                if(self.matriz[c][f] > 0):
                    lista_adyacencia[f][c] = self.vertices[c]
        return lista_adyacencia
    # BFS
    def bfs(G, s):
        n = len(G)
        print(n)
        path = [" "]*n
        visited = [False]*n
        queue = [s]
        visited[s] = True
        while len(queue) > 0:
            u = queue[0]
            queue = queue[1:]
            for v in G[u]:
                if not visited[v]:
                    queue.append(v)
                    path[v] = u
                    visited[v] = True
        return path