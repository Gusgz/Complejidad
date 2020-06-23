class Util:
    def rotar_matriz(matriz):
        m = []
        for f in range(2):
            m.append([])
            for c in range(2):
                m[f].append(matriz[len(matriz)-1-c][f])
        return m
