import random


def main():
    v = []
    for i in range(0, random.randint(1, 10)):
        n = random.randint(0, 100)
        v.append(n)
    x = random.choice(v)
    v = sorted(v)

    # v = [6, 21, 23, 28, 33, 57, 57, 90, 96]
    # x = 96

    print(f'Condições iniciais: {v} {x}\n')
    print(f'\nResposta:{busca_binariaR(v, x)}')


def busca_binariaR(v, x):
    """
    Erro: retorna index baseado na fatia que está na busca binária!
    """
    n = len(v)
    if n == 0:
        return None
    m = n // 2

    print(f'Fatia atual: {v} || {x}')
    print(f'm = {m}')
    print(f'v[{m}] = {v[m]}\n')

    if v[m] == x:
        return m

    if v[m] < x:
        return m + 1 + busca_binariaR(v[m + 1:], x)
    else:
        return busca_binariaR(v[:m], x)


main()
