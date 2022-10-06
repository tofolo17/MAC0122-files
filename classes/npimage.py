import numpy as np


def main():
    arr = np.array(range(9)).reshape(3, 3)
    a = NPImagem((), arr)

    brr = np.array(range(16)).reshape(4, 4)
    b = NPImagem((), brr)

    print(a.data)
    print(b.data)

    print()

    print(a + b)


class NPImagem:
    def __init__(self, key=(0, 0), val=0):
        if type(val) is np.ndarray:
            self.data = val
        else:
            self.data = np.full(key, val)
        self.shape = self.data.shape

    def __str__(self):
        return str(self.data)

    def __getitem__(self, key):
        lin, col = key
        return self.data[lin, col]

    def __setitem__(self, key, val):
        lin, col = key
        self.data[lin, col] = val

    def crop(self, sup=0, esq=0, inf=None, dire=None):
        if inf is None:
            inf = self.shape[0]
        if dire is None:
            dire = self.shape[1]
        nw = self.data[sup:inf, esq:dire]  # Fatias são vistas
        ni = NPImagem(self.shape, nw)
        return ni

    def pinte_rect(self, sup, esq, inf, dire, v=0):
        # Correções (sup, esq)
        if sup < 0:
            sup = 0
        if esq < 0:
            esq = 0

        # Correções (inf, dire)
        nl, nc = self.shape
        if dire > nc - 1:
            dire = nc
        if inf > nl - 1:
            inf = nl

        self.data[sup:inf, esq:dire] = v

    def paste(self, other, sup, esq):
        sl, sc = self.shape
        ol, oc = other.shape

        # Armazenando valores originais
        sup_o, esq_o = sup, esq

        # Exceções
        if sup > sl - 1 or esq > sc - 1:
            return None
        if sup + ol - 1 < 0 or esq + oc - 1 < 0:
            return None

        dire = esq + oc - 1
        inf = sup + ol - 1

        # Correção da coluna
        if esq < 0:
            esq = 0
        if dire > sc - 1:
            dire = sc - 1
        # Se não, está em self

        # Correção da linha
        if sup < 0:
            sup = 0
        if inf > sl - 1:
            inf = sl - 1
        # Se não, está em self

        # Declarações do other
        o_sup = sup - sup_o
        o_esq = esq - esq_o
        o_inf = inf - sup_o
        o_dire = dire - esq_o

        self.data[sup:inf + 1, esq:dire + 1] = other.data[o_sup:o_inf + 1, o_esq:o_dire + 1]

    def get_pos(self, key):
        return key // self.shape[1], key % self.shape[1]

    # TODO: reestruturar código. Está errado! É pra somar só nas coordenadas correspondentes, sem realocação.
    def __add__(self, other):
        s_size = self.shape[0] * self.shape[1]
        if type(other) in [int, float]:
            for i in range(s_size):
                ls, cs = self.get_pos(i)

                self.data[ls, cs] += other
        else:
            o_size = other.shape[0] * other.shape[1]
            for i in range(min(o_size, s_size)):
                ls, cs = self.get_pos(i)
                lo, co = other.get_pos(i)

                self.data[ls, cs] += other.data[lo, co]

        return NPImagem((), self.data[:])

    def __mul__(self, other):
        s_size = self.shape[0] * self.shape[1]
        if type(other) in [int, float]:
            for i in range(s_size):
                ls, cs = self.get_pos(i)

                self.data[ls, cs] *= other
        else:
            o_size = other.shape[0] * other.shape[1]
            for i in range(min(o_size, s_size)):
                ls, cs = self.get_pos(i)
                lo, co = other.get_pos(i)

                self.data[ls, cs] *= other.data[lo, co]

        return NPImagem((), self.data[:])

    # Só isso mesmo?
    def blend(self, other, alpha=0.5):
        return self * alpha + other * (1 - alpha)


if __name__ == '__main__':
    main()
