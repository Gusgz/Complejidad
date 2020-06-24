class Util:

    @staticmethod
    def rotar_matriz(self,matriz):
        m = []
        for f in range(len(matriz[0])):
            m.append([])
            for c in range(len(matriz)):
                m[f].append(matriz[len(matriz)-1-c][f])
        return m