n = int(input('Quantidade de valores na lista: '))

lista = []
for i in range(n):
    v = int(input(f'{i + 1}° valor: '))
    lista += [v]

minimo = 0
indice = 0
for i in range(len(lista)):
    v = lista[i]

    if i == 0:
        minimo = v
    if v < minimo:
        minimo = v
        indice = i

if __name__ == "__main__":
    main()
