def main():
    h = MaxHeap()
    v = [1, 4, 5, 3, 6]
    h.construa(v)
    print(h.data)

    print(h.remova())
    print(h.data)

    print(h.remova())
    print(h.data)


class MaxHeap:
    """
    É uma árvore binária. Uma árvore é max-heap se para todo nó,
    com exceção da raiz, o valor da mãe é maior ou igual o valor das filhas.
    """

    def __init__(self):
        self.data = [None]

    def __str__(self):
        # Que gambiarra feia!
        v = self.data[1:]

        s = ''
        m, j = 0, 0
        for el in v:
            s += f'{el}\t'
            if j % (2 ** m) == 0:
                j = 0
                m += 1
                s += '\n'

            j += 1

        return s

    def __len__(self):
        return len(self.data[1:])

    def vazio(self):
        return len(self.data) == 1

    def insira(self, item):
        # acrescenta o item no final da lista
        self.data.append(item)

        # pega esta última posição
        pos = len(self.data) - 1

        if self.vazio():
            self.data.append(item)
            return

        el = self.data[pos // 2]
        while el is not None and el < item:
            self.data[pos // 2], self.data[pos] = self.data[pos], self.data[pos // 2]
            pos = pos // 2

            el = self.data[pos // 2]

    def remova(self):
        """(MaxHeap) -> obj
        RECEBE um MaxHeap self.
        REMOVE e RETORNA o maior elemento do MaxHeap.
            Após o remover o maior elemento o MaxHeap é consertado
        """
        # crie apelidos
        n = len(self.data)  # 1 a mais que o número de itens no MaxHeap
        dt = self.data  # itens: dt[1], dt[2],...,dt[n-1]

        # MaxHeap vazio: erro
        if n == 1:
            print("MaxHeap ERRO: tentativa de remoção em max-heap vazio")
            return None

        # MaxHeap tem apenas 1 ‘item’
        if n == 2:
            return dt.pop()

        # MaxHeap tem pelo menos dois itens
        item = dt[1]
        dt[1] = dt.pop()

        # arrume MaxHeap
        n = n - 1
        mae = 1  # mãe
        filha = 2  # filha
        valor = dt[mae]

        # selecione a maior das duas filhas
        if filha < n - 1 and dt[filha] < dt[filha + 1]:
            filha += 1

        while filha < n and valor < dt[filha]:
            dt[mae] = dt[filha]  # elemento da filha sobe
            mae = filha  # mãe desce
            filha = 2 * mae  # filha esquerda

            # selecione a maior das duas filhas
            if filha < n - 1 and dt[filha] < dt[filha + 1]:
                filha += 1

        dt[mae] = valor
        return item

    def construa(self, v):
        for el in v:
            self.insira(el)

    def maxheap(self):
        """ (MaxHeap) -> bool
        RECEBE um MaxHeap self.
        RETORNA True se self.data representa um max-heap e False
            em caso contrário.
        """
        # apelidos
        n = len(self.data)
        dt = self.data

        # deve ter pelo menos None
        if n == 0:
            return False

        # primeira posição deve ser None
        if dt[0] is not None:
            return False

        # verifique se satisfaz a propriedade/invariante de max-heap
        for filha in range(2, n):
            mae = filha // 2

            # mãe deve ser maior ou igual à filha
            if dt[mae] < dt[filha]:
                return False

        return True


def selecione_lst(v, n):
    """ (list, int) -> int
    RECEBE uma lista v.
    RETORNA um índice i tal que v[i] é o maior elemento de v[0:n]
    """
    imax = n - 1
    for i in range(n - 1):
        if v[i] > v[imax]: imax = i
    return imax


def selection_sort(v):
    """(list) -> None
    RECEBE uma lista v.
    REARRANJA os elementos de v para que fiquem em ordem crescente.

    Possui complexidade O(n^2). O espaço necessário extra é constante.
    """
    n = len(v)
    print(f'Lista de entrada: {v} | Tamanho: {n}')

    for i in range(n, 1, -1):
        # selecione a posição de um maior elemento da vista v[0: i]
        imax = selecione_lst(v, i)
        print(f'Posição de um maior elemento: {imax} | Index: {i}')
        # mova o maior elemento para a última posição da vista v[0: i]
        v[i - 1], v[imax] = v[imax], v[i - 1]
        print(f'Lista após iteração: {v}\n')


def heapsort(v):
    """(list) -> None
    RECEBE uma lista v.
    REARRANJA os elementos de v para que fiquem em ordem crescente.
    NOTA. Usa a classe MaxHeap. Adaptação mutante de heapsort() em
        https://docs.python.org/3/library/heapq.html
    """
    n = len(v)
    # pré-processamento: crie um MaxHeap com elementos de v
    h = MaxHeap()
    for item in v:
        h.insira(item)

    # ordenação por seleção
    for i in range(n, 1, -1):
        # maior elemento da lista v[0: i] vai para última posição da lista
        v[i - 1] = h.remova()


main()
