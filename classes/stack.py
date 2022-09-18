class Pilha:
    def __init__(self):
        self.dados = []

    def __len__(self):
        return len(self.dados)

    def vazia(self):
        return self.dados == []

    def empilhe(self, item):
        self.dados.append(item)

    def desempilhe(self):
        return self.dados.pop()

    def topo(self):
        return self.dados[-1]
