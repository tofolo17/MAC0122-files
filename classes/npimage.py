import numpy as np


def main():
    # Declarações
    a = NPImagem((3, 3), 0)
    b = NPImagem((3, 3), 1)

    print('Testes pinte_rect()')
    print(f'Imagem A:\n{a}\n')

    print(f'Imagem A pintada:')
    a.pinte_rect(1, 1, 7, 7, 1)
    print(f'{a}\n')

    print('Testes paste()')
    print(f'Exceções')
    a.paste(b, 3, 3)
    print(f'paste() após a imagem:\n{a}\n')

    a.paste(b, -3, -3)
    print(f'paste() antes a imagem:\n{a}\n')

    a = NPImagem((0, 0), np.array(range(9)).reshape(3, 3))
    b = NPImagem((0, 0), np.array(range(9)).reshape(3, 3))

    print(f'Intersecções')
    a.paste(b, -1, 1)
    print(f'Finalmente:\n   {a}')


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

        # Coordenadas que restringem intersecção
        print('Para o self:')
        print(f'(sup, esq) = ({sup},{esq})')
        print(f'(inf, dire) = ({inf},{dire})\n')

        # Mesmas coordenadas em relação ao other
        print('Para o other:')
        print(f'(sup, esq) = ({sup - sup_o},{esq - esq_o})')
        print(f'(inf, dire) = ({inf - sup_o},{dire - esq_o})\n')

        # Declarações do other
        o_sup = sup - sup_o
        o_esq = esq - esq_o
        o_inf = inf - sup_o
        o_dire = dire - esq_o

        self.data[sup:inf + 1, esq:dire + 1] = other.data[o_sup:o_inf + 1, o_esq:o_dire + 1]


if __name__ == '__main__':
    main()
