def main():
    img1 = PyImage(2, 2)
    print(img1)

    img2 = PyImage(2, 2, ['a', 'b', 'c', 'd'])
    print(img2)

    print()

    print(img1.paste(img2, 2, 2))
    print(img1.paste(img2, -2, 0))

    print(img1.paste(img2, -1, 0))


class PyImage:
    def __init__(self, n_lins, n_cols, valores=None):
        self.linhas = n_lins
        self.colunas = n_cols
        self.data = []

        c = 0
        for i in range(self.linhas):
            linha = []
            for j in range(self.colunas):
                if valores is None:
                    linha += [0]
                else:
                    linha += [valores[c]]
                c += 1
            self.data.append(linha)

    def paste(self, other, t_lin, t_col):
        # Exceções
        if t_lin > self.linhas - 1 or t_col > self.colunas - 1:
            return self
        if t_lin + other.linhas - 1 < 0 or t_col + other.colunas < 0:
            return self

        # Intersecções
        for i in range(other.linhas):
            inter_l = t_lin + i
            for j in range(other.colunas):
                inter_c = t_col + j

                if 0 <= inter_l < self.linhas and 0 <= inter_c <= self.colunas:
                    print(inter_l, inter_c)  # Verifica intersecção

    def __str__(self):
        return f'{self.data}'


main()
