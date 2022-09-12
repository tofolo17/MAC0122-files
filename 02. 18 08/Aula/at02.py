def main():
    lista = [1, -3.14, 'um', 'um', 1, 'um']
    print(conta_palavras(lista))


def conta_palavras(lista):
    unicos = []
    for el in lista:
        if el not in unicos:
            unicos += [el]

    occor = [0] * len(unicos)
    for i in range(len(occor)):
        for j in range(len(lista)):
            if unicos[i] == lista[j]:
                occor[i] += 1

    return unicos, occor


if __name__ == "__main__":
    main()
