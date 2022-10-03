def main():
    lm1 = ListaMaluca()
    print(lm1)

    lm2 = ListaMaluca([3, 4, True, 3, 3, 3, 3])
    print(lm2)

    lm3 = ListaMaluca([0, 0, 0, 4, True])
    lm_2_3 = lm2 + lm3
    print(lm_2_3)

    lm_3_2 = lm3 + lm2
    print(lm_3_2)

    print(lm3 * 3)
    print(3 * lm3)


class ListaMaluca:
    def __init__(self, valores=None):
        """
        self.valores = valores, com valores=[] está errado?
        """
        if valores is None:
            valores = []
        self.data = valores

    def __str__(self):
        return f'{self.data}'

    def __add__(self, other):
        ta = len(self.data)
        tb = len(other.data)
        maior, menor = self, other
        if tb > ta:
            maior, menor = other, self

        n = []
        for i in range(len(menor.data)):  # Não precisava verificar paridade
            n += [self.data[i]]
            n += [other.data[i]]

        n += maior.data[len(menor.data):]
        return ListaMaluca(n)

    def __mul__(self, other):
        if type(other) == int:
            n = []
            for char in self.data:
                for i in range(other):
                    n += [char]

            return ListaMaluca(n)
        pass

    def __rmul__(self, other):
        return self * other


main()

'''
a, b, c
1, 2, 3, 4, 5

a, 1, b, 2, c, 3, 4, 5
1, a, 2, b, 3, c, 4, 5



'''
