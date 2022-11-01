"""
def busca_bin(v, x):
    ''' (list, obj) -> int ou None
    RECEBE uma lista v e um objeto x.
    RETORNA um índice i tal que v[i] == x.
        Se o x não está na lista a função retorna None.
    PRÉ-CONDIÇÃO: supõe que a lista é crescente.
    '''


n = len(v)
e = 0
d = n
while e < d:  # 1#
    m = (e + d) // 2
    if v[m] == x: return m
    if v[m] < x:
        e = m + 1
    else:
        d = m
return None
"""
import random


def main():
    v = []
    for i in range(0, random.randint(1, 10)):
        n = random.randint(0, 100)
        v.append(n)
    x = random.randint(0, 100)
    v = sorted(v)
    # print(v, x)

    # v = [0, 15, 16, 21, 36, 56, 61, 77, 80]
    # x = 16

    print(f'\nResposta:{busca_binaria(v, x)}')


def busca_binaria(v, x, e=0, d=None):
    if d is None:
        d = len(v)

    print(f'Condições iniciais: {v} {x}\n')

    if x < v[0]:
        return -1

    if x > v[-1]:
        return len(v) - 1

    i = 0
    while e < d:
        m = (e + d) // 2
        print(f'Na {i + 1}° iteração:\nm = {m}')

        print(f'v[{m}] = {v[m]}')
        if x < v[m]:
            d = m
        if x > v[m]:
            e = m + 1
        if v[m] == x or v[m] < x < v[m + 1]:
            return m

        i += 1
        pause()

    return -1


def pause():
    input()


main()
