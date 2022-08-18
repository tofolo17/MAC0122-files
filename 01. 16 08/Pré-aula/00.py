def main():
    base = float(input("Digite a base real: "))
    exp = int(input("Digite o expoente inteiro: "))
    pot = potencia(base, exp)
    print(f"potencia({base}, {exp}) = {pot} \n")


def potencia(base, expoente):
    """ (float, int) -> float
    retorna a base elevado ao expoente inteiro """

    r = 1
    for i in range(expoente):
        r *= base

    return r  # base ** expoente


# chama a função main()
if __name__ == "__main__":
    main()
