def main():
    n = int(input('n: '))
    m = int(input('m: '))

    print(combinacao(m, n))


def fatorial(v):
    r = 1
    for i in range(v, 0, -1):
        r *= i

    return r


def combinacao(m, n):
    # Obs.: m > n
    return fatorial(m) / (fatorial(n) * fatorial(m - n))


if __name__ == "__main__":
    main()
