class Grafo:
    def __init__(self):
        self.vertices = []
        self.matriz = [[0]*0 for i in range(0)]
        self.colores = []

    def agregar_vertice(self,vertice,color):
        self.vertices.append(vertice)
        self.colores.append(color)
        n = len(self.vertices)
        matriz_aux = [[0]*n for i in range(n)]
        for f in range(len(self.matriz)):
            for c in range(len(self.matriz)):
                matriz_aux[c][f] = self.matriz[c][f]
        self.matriz = matriz_aux
        return
    
    def agregar_arista(self,inicio,final,valor):
        self.matriz[self.vertices.index(final)][self.vertices.index(inicio)] = valor

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

    def generar_lista(self):
        n = len(self.vertices)
        lista = [[]*n for i in range(n)]
        for f in range(len(self.matriz)):
            x = f*6
            for c in range(len(self.matriz)):
                if self.matriz[c][f] > 0:
                    lista[f].append((self.vertices[x+c],self.matriz[c][f]))
        return lista
 
    def re_dfs(G,u,visited,path,n):
        if visited[u] != True:
            visited[u] = True
            for v in range(len(G)):
                if G[u][v] != 0 and visited[v] != True:
                    path[v] = u
                    re_dfs(G,v,visited,path,n)

    def dfs(G,s):
        n = len(G)
        visited = [False]*n
        path = [None]*n
        re_dfs(G,s,visited,path,n)
        return path

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

    
    