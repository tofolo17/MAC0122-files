class DicioB:
    def __init__(self):
        self.chaves = []
        self.valores = []

    def __str__(self):
        s = ''

        # apelidos
        n = len(self)

        chaves = self.chaves
        valores = self.valores

        for i in range(n):
            s += f"{chaves[i]}: {valores[i]}\n"
        return s

    def put(self, chave, valor):
        if chave in self.chaves:
            i = self.chaves.index(chave)
            self.valores[i] = valor
        else:
            self.chaves += [chave]
            self.valores += [valor]
            self._ordena()

    def get(self, chave):
        if chave in self.chaves:
            # TODO: aplicar busca binária para adquirir este index.
            i = self.chaves.index(chave)
            return self.valores[i]
        return None

    # TODO: Revisar funcionamento.
    def _ordena(self):
        n = len(self.chaves)
        for i in range(1, n):
            x = self.chaves[i]
            y = self.valores[i]
            j = i - 1
            while j >= 0 and self.chaves[j] > x:
                self.chaves[j + 1] = self.chaves[j]
                self.valores[j + 1] = self.valores[j]
                j -= 1

            self.chaves[j + 1] = x
            self.valores[j + 1] = y

    def __len__(self):
        return len(self.chaves)

    def __setitem__(self, chave, valor):
        self.put(chave, valor)

    def __getitem__(self, chave):
        return self.get(chave)

    def __contains__(self, chave):
        return chave in self.chaves

    def __iter__(self):
        return iter(self.keys())

    def keys(self):
        return self.chaves[:]

    def values(self):
        return self.valores[:]

    def items(self):
        lst = []

        # apelidos
        n = len(self)
        chaves = self.chaves
        valores = self.valores

        for i in range(n):
            lst += [(chaves[i], valores[i])]
        return lst


def main():
    print("Testes para a classe DicioB")
    print("--------------------------\n")

    # __init__() e __str__()
    print("crie um dicionário vazio")
    dB = DicioB()
    print(f"dB:\n{dB}")
    pause()  # aprecie a paisagem

    # put()
    print("\nteste put()")
    dB.put('fracassei', 3)
    dB.put('em', 1)
    dB.put('tudo', 1)
    print(f"dB:\n{dB}")
    pause()  # aprecie a paisagem

    # __setitem__()
    print("\nteste __setitem__()")
    dB['o'] = 2
    dB['que'] = 3
    dB['tentei'] = 4
    print(f"dB:\n{dB}")
    pause()  # aprecie a paisagem

    # put() e __setitem__()
    print("\nteste put() e __setitem__()")
    dB.put('o', 2)
    dB['que'] = 1
    dB['tentei'] = 5
    print(f"dB:\n{dB}")
    pause()  # aprecie a paisagem

    # get()
    print("\nteste get()")
    print(f"dB.get('fracassei')={dB.get('fracassei')}")
    print(f"dB.get('em')={dB.get('em')}")
    print(f"dB.get('tudo')={dB.get('tudo')}\n")
    pause()  # aprecie a paisagem

    # __getitem__()
    print("\nteste __getitem__()")
    print(f"dB['o']={dB['o']}")
    print(f"dB['que']={dB['que']}")
    print(f"dB['tentei']={dB['tentei']}")
    print(f"dB.get('vida')={dB.get('vida')}")
    print(f"dB['vida']={dB['vida']}\n")
    pause()  # aprecie a paisagem

    # mais __setitem__()
    print("\nmais teste __setitem__(): chaves devem ser comparáveis por <, <=,...")
    dB['na'] = 1
    dB['vida'] = 1
    print(f"dB:\n{dB}")
    pause()  # aprecie a paisagem

    # teste __contains__()
    print("\nteste __contains__()")
    print(f"'tentei' in dB={'tentei' in dB}")
    print(f"'1' in dB={'1' in dB}")
    print(f"1 in d={1 in dB}")
    print(f"5 in d={5 in dB}\n")
    pause()  # aprecie a paisagem

    # teste __iter__()
    print("\nteste __iter__(): usado para clonar d")
    clone = DicioB()
    for chave in dB: clone[chave] = dB[chave]
    print(f"clone:\n{clone}")
    pause()  # aprecie a paisagem

    # teste __len__()
    print("\nteste __len__()")
    print(f"len(dB)={len(dB)}")
    print(f"len(clone)={len(clone)}")
    dicio_vazio = DicioB()
    print(f"len(dicio_vazio)={len(dicio_vazio)}\n")
    pause()  # aprecie a paisagem

    # teste keys(), values() e items()
    print("\nteste keys(), values() e items()")
    print(f"clone.keys()={clone.keys()}")
    print(f"clone.values()={clone.values()}")
    print(f"clone.items()={clone.items()}\n")
    pause()  # aprecie a paisagem

    print("FIM")


# -----------------------------------------------
def pause():
    input("Tecle ENTER para continuar: ")


# -----------------------------------------------
if __name__ == "__main__":
    main()
