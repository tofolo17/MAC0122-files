"""
Era só usar o operador para a string toda...

Valeu a tentativa :D
"""


def main():
    lista = ['cachorro', 'amigo', 'cachorra', 'cabo', 'azul']

    minimo, pos = menor_alfabetica(lista)

    print(minimo, pos)


def menor_alfabetica(lista):
    # Achar tamanho da maior palavra
    tamanho_maximo = 0
    for palavra in lista:
        tamanho_palavra = len(palavra)

        if tamanho_palavra > tamanho_maximo:
            tamanho_maximo = tamanho_palavra

    # Transformando as palavras
    lista_transformada = []
    for palavra in lista:
        palavra_transformada = [' '] * 8

        for i in range(len(palavra)):
            palavra_transformada[i] = palavra[i]

        lista_transformada.append(palavra_transformada)

    # Compara os índices
    pos = 0
    menor_palavra = lista_transformada[pos]
    for i in range(1, len(lista_transformada)):
        palavra_atual = lista_transformada[i]

        j = 0
        flag = False
        while j < tamanho_maximo and not flag:
            char_atual = palavra_atual[j]
            char_menor = menor_palavra[j]

            if char_atual < char_menor:
                menor_palavra = palavra_atual
                pos = i
                flag = True
            elif char_atual > char_menor:
                flag = True

            j += 1

    return lista[pos], pos


if __name__ == "__main__":
    main()
