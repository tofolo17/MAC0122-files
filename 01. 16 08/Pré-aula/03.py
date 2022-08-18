def main():
    n = int(input('n: '))
    m = int(input('m: '))

    print(mdc_fb(m, n))


def mdc_fb(m, n):
    # algoritmo força bruta --> mdc
    i = n
    while not (m % i == 0 and n % i == 0):
        i -= 1

    return i


if __name__ == "__main__":
    main()
