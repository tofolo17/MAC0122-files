class Rede:
    def __init__(self, n_lins, n_cols, N=None):
        if N:
            self.matriz = N
        else:
            M = []
            for i in range(n_lins):
                L = []
                for j in range(n_cols):
                    L += ['X']
                M.append(L)
            self.matriz = M[:]

    def abra(self, positions):
        for pos in positions:
            l, c = pos[0], pos[1]
            self.matriz[l][c] = '0'

    def clone(self):
        return Rede(0, 0, self.matriz)

    def tem_caminho(self):
        for j in range(len(self.matriz[0])):
            if self.matriz[0][j] == '0':
                r = self.procura_caminho(0, j)
                if r:
                    return True
        return False

    def procura_caminho(self, i, j, caminhos=None):
        if caminhos is None:
            caminhos = list()

        caminhos.append([i, j])

        # Caso base
        if i == len(self.matriz) - 1:
            return True

        # Caso recursivo sem limitadores
        if self.matriz[i + 1][j] == '0' and [i + 1, j] not in caminhos:
            return self.procura_caminho(i + 1, j, caminhos)

        # Caso recursivo com limitadores
        if i != 0:
            if self.matriz[i - 1][j] == '0' and [i - 1, j] not in caminhos:
                return self.procura_caminho(i - 1, j, caminhos)
        if j != 0:
            if self.matriz[i][j - 1] == '0' and [i, j - 1] not in caminhos:
                return self.procura_caminho(i, j - 1, caminhos)
        if j != len(self.matriz[0]) - 1 and i != 0:  # Só precisa ir para lado se a linha diferir da primeira!
            if self.matriz[i][j + 1] == '0' and [i, j + 1] not in caminhos:
                return self.procura_caminho(i, j + 1, caminhos)
        return False


def main():
    r = Rede(4, 6)

    r.abra([[1, 0], [0, 0], [3, 5], [2, 2], [2, 3], [1, 1], [2, 5], [1, 4]])
    r.abra([[2, 1], [1, 3], [1, 5], [0, 2], [3, 0]])

    print(r.tem_caminho())


main()
