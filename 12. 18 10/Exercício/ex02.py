def main():
    print(somaR([3, 3, 2], 3))


def somaR(v, n):
    if n == 0:
        return 0
    return somaR(v[1:],n) + v[0]

main()
