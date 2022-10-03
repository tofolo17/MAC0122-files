import numpy as np


def main():
    print('NPImagem a)')
    a = NPImagem((3, 3))
    print(a.data)
    print()

    print('NPImagem b)')
    lst_b = list(range(9))
    arr_b = np.array(lst_b).reshape(3, 3)
    b = NPImagem(arr_b.shape, arr_b)  # Porque (0, 0) no exemplo?
    print(b.data)
    print()

    print('NPImagem c), vista de b)')
    c = b.crop()
    print(c.data)
    print()

    print('NPImage b) alterada')
    b[0, 0] = 1
    print(b.data)
    print()

    print('NPImagem c) também alterado, por ser vista')
    print(c.data)
    print()

    print('NPImagem d), corte de c)')
    d = c.crop(1, 1)
    print(d.data)


class NPImagem:

    def __init__(self, shape=(0, 0), val=None):
        if type(val) is np.ndarray:
            self.data = val
        else:
            if val is None:
                val = 0
            self.data = np.full(shape, val)
        self.shape = self.data.shape

    def __str__(self):
        return str(self.data)

    def __getitem__(self, key):
        return self.data[key[0], key[1]]

    def __setitem__(self, key, valor):
        self.data[key[0], key[1]] = valor

    def crop(self, sup=0, esq=0, inf=None, dire=None):
        if inf is None:
            inf = self.shape[0]
        if dire is None:
            dire = self.shape[1]
        nw = self.data[sup:inf, esq:dire]  # Fatias são vistas
        ni = NPImagem(self.shape, nw)
        return ni


main()
