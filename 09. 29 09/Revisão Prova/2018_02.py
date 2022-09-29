def main():
    v = 4.4
    n = 1000

    print(forca_bruta(v, n))
    print(esperta(v, n))


def f(x):
    return x ** 0.5


def forca_bruta(v, n):
    contador = 0

    menor_k = 0
    menor_diff = 0
    for k in range(n + 1):
        diff = abs(f(k) - v)
        contador += 1

        if diff < menor_diff or menor_k == 0:
            menor_diff = diff
            menor_k = k

        if menor_diff == 0:
            return menor_k, menor_diff, contador

    return menor_k, menor_diff, contador


def esperta(v, n):
    LI = 0
    LS = n

    c = 0
    while LI <= LS:
        c = (LS + LI) // 2
        if f(c) == 0:
            return c
        elif f(c) - v < 0:
            LI = c + 1
        else:
            LS = c - 1

    return c


main()
