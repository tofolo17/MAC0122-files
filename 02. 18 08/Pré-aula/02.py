def main():
    # Obs.: \n é apenas 1 caracter

    texto = "  \n \n , teste, ola ola.."  # input()
    print(palavras(texto))


def palavras(texto):
    p = []
    sep = ["\n", "\t", " ", ",", ".", ";"]

    texto += ' '
    t = len(texto)

    inicio = -1
    em_palavra = False
    for i in range(t):
        char = texto[i]
        if char not in sep:
            if not em_palavra:
                inicio = i
            em_palavra = True
        else:
            if inicio != -1:
                p.append(texto[inicio: i])

            inicio = -1
            em_palavra = False

    return p


if __name__ == "__main__":
    main()
