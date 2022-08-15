def main():
    n = int(input('Números na sequência: '))
    while not n > 0:
        n = int(input('Números na sequência: '))

    maximo = minimo = 0
    for i in range(n):
        v = int(input(f'{i + 1}° valor: '))
        if i == 0:
            maximo = v
            minimo = v
        if v > maximo:
            maximo = v
        if v < minimo:
            minimo = v

    print(f'Máximo: {maximo}\nMínimo: {minimo}')


if __name__ == "__main__":
    main()
