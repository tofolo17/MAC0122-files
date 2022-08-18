def main():
    # Obs.: \n é apenas 1 caracter

    texto = ' isto é um, teste\n; ok'  # input()
    print(palavras(texto))


def palavras(texto):
    sep = ["\n", "\t", " ", ",", ".", ";"]
    comp = []
    p = []

    t = len(texto)

    inicio = -1
    em_palavra = False
    for i in range(t):
        char = texto[i]
        if char not in sep:
            if not em_palavra:
                inicio = i
            comp += [inicio]
            em_palavra = True
        else:
            if inicio != -1:
                p.append(texto[inicio: i])

            inicio = -1
            comp += [inicio]
            em_palavra = False

    if inicio != -1:
        p.append(texto[inicio:t])

    return p


if __name__ == "__main__":
    main()
