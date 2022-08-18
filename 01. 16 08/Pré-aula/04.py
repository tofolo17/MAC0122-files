def main():
    n = 18
    m = 24

    print(mdc(m, n))


def mdc(m, n):
    while m % n != 0:
        temp = n
        n = m % n
        m = temp

    return n


if __name__ == "__main__":
    main()
