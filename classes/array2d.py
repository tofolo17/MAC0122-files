# Testes de aula obrigatórios para envio

def main():
    print("Testes da classe Array2D\n")

    a = Array2D((2, 3), 3)  # cria Array2D com valor inicial 3
    print(f'teste 1: Criação do Array2D a:')
    print(a)
    print(f'shape: {a.shape}')
    print(f'size : {a.size}')
    print(f'data : {a.data}')
    print()

    b = Array2D((2, 3), 1.7)  # criar Array2D com valor inicial 1.7
    print(f'teste 2: Criação do Array2D b:')
    print(b)
    print(f'shape: {b.shape}')
    print(f'size : {b.size}')
    print(f'data : {b.data}')
    print()

    print(f'teste 3: a[0,1] + 100 é: {a[0, 1] + 100}')  # acesso direto usando tupla: use o método __getitem__
    print()

    a[1, 1] = -1  # atribuição usando tupla: use o método __setitem__
    print(f'teste 4: Array2D a:')
    print(a)


class Array2D:
    def __init__(self, shape: tuple, val):
        self.shape = shape
        self.size = self.shape[0] * self.shape[1]
        self.data = [val] * self.size

    def reshape(self, shape):
        a = Array2D(shape, 0)
        a.data = self.data

        return a

    def copy(self):
        a = Array2D(self.shape, 0)
        a.data = self.data[:]

        return a

    def __getitem__(self, key):
        return self.data[self.shape[1] * key[0] + key[1]]

    def __setitem__(self, key, valor):
        self.data[self.shape[1] * key[0] + key[1]] = valor

    def __str__(self):
        s = ""
        for i in range(1, self.size + 1):
            if i % self.shape[1] == 0:
                s += f'{self.data[i - 1]} \n'
            else:
                s += f'{self.data[i - 1]} '

        return s

    def __add__(self, other):
        # Assume Array2D's de mesmo shape
        res = Array2D(self.shape, 0)
        for i in range(len(self.data)):
            if type(other) == int or type(other) == float:
                res.data[i] = self.data[i] + other
            else:
                res.data[i] = self.data[i] + other.data[i]
        return res

    def __sub__(self, other):
        # Assume Array2D's de mesmo shape
        res = Array2D(self.shape, 0)
        for i in range(len(self.data)):
            if type(other) == int or type(other) == float:
                res.data[i] = self.data[i] - other
            else:
                res.data[i] = self.data[i] - other.data[i]
        return res

    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        return -(self - other)

    def __neg__(self):
        res = Array2D(self.shape, 0)
        for i in range(len(self.data)):
            res.data[i] = -self.data[i]
        return res


if __name__ == '__main__':
    main()
