def main():
    a = Array3D((2, 3, 4))

    data = list(range(2 * 3 * 4))
    a.carregue_copia(data)

    print(a.data, a[1, 2, 3])

    print(a.get_pos(18))


class Array3D:
    def __init__(self, shape, val=None):
        if val is None:
            val = []
        self.andares, self.linhas, self.colunas = shape
        self.size = self.andares * self.linhas * self.colunas
        self.data = val

    def carregue_vista(self, new_data):
        self.data = new_data

    def carregue_copia(self, new_data):
        self.data = new_data[:]

    def __getitem__(self, item):
        andar, linha, coluna = item
        k2 = self.colunas * linha + coluna
        k = andar * self.linhas * self.colunas + k2

        return self.data[k]

    def get_pos(self, k):
        andar = k // (self.linhas * self.colunas)  # correto
        linha = (k - andar * self.linhas * self.colunas) // self.colunas  # correto
        coluna = (k - andar * self.linhas * self.colunas) % self.colunas  # feito incorreto na prova

        return andar, linha, coluna


main()
