def main():
    linhas = 2
    colunas = 3

    a = Matriz(linhas, colunas, 10)
    print(a.data)

    print(a)


class Matriz:
    def __init__(self, n_lins, n_cols, val=0):
        self.linhas = n_lins
        self.colunas = n_cols
        self.data = []
        for i in range(n_lins):
            linha = []
            for j in range(n_cols):
                linha += [val]
            self.data.append(linha)

    def carregue(self, data):
        c = 0
        for i in range(self.linhas):
            for j in range(self.colunas):
                self.data[i][j] = data[c]
                c += 1

    def __add__(self, other):
        if type(other) == Matriz:
            new_data = []
            for i in range(self.linhas):
                for j in range(self.colunas):
                    new_data += [self.data[i][j] + other.data[i][j]]

            a = Matriz(self.linhas, self.colunas)
            a.carregue(new_data)

            return a
        pass

    def __mul__(self, other):
        if type(other) in [float, int]:
            new_data = []
            for i in range(self.linhas):
                for j in range(self.colunas):
                    new_data += [self.data[i][j] * other]

            a = Matriz(self.linhas, self.colunas)
            a.carregue(new_data)

            return a
        pass

    def __str__(self):
        s = ''
        for i in range(self.linhas):
            for j in range(self.colunas):
                s += f'{self.data[i][j]:5d}'
            s += '\n'

        return s[:-1]


main()
