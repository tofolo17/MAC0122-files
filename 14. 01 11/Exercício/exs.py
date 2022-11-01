def buscaA(v, x):
    n = len(v)
    for i in range(n):
        if v[i] == x:
            return i
    return None


def buscaB(v, x):
    e, d = 0, len(v)
    while e < d:
        m = (e + d) // 2
        if v[m] == x:
            return m
        if v[m] < x:
            e = m + 1
        else:
            d = m
    return None


def crie_dicionario(lst, n):
    dicio = Dicio()
    for i in range(n):
        chave = lst[i]
        valor = dicio.get(chave)
        if valor is None:
            dicio[chave] = 1
        else:
            dicio[chave] = valor + 1
    return dicio


def main():
    print(buscaB([10, -5, 5, 3, 12], 5))


main()
