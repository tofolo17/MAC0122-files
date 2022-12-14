from classes.stack import Pilha


def main():
    s = "luz azul"
    print(pal(s))

    print(pal_internet(s))


def pal(s) -> bool:
    """
    Erros:
        — Esquecer retorno de Pilha().desempilha();
        — Esquecer método vazia().
    """
    empilha = Pilha()
    desempilha = Pilha()

    i = 0
    while i < len(s):
        char = s[i]
        if char != ' ':
            empilha.empilhe(s[i])
        i += 1
    s_empilha = empilha.dados.copy()

    i = 0
    while i < len(s_empilha):
        desempilha.empilhe(empilha.topo())
        empilha.desempilhe()
        i += 1
    s_desempilha = desempilha.dados

    return s_empilha == s_desempilha


def pal_internet(s):
    pilha = Pilha()
    for char in s:
        pilha.empilhe(char)

    reversed_text = ""
    while not pilha.vazia():
        reversed_text += pilha.desempilhe()

    return s == reversed_text


def pal_mencarini(s):
    pil = Pilha()
    desempilha = Pilha()

    for letra in s:
        pil.empilhe(letra)
    sentido1 = pil.dados.copy()

    while pil.vazia() is False:
        desempilha.empilhe(pil.topo())
        pil.desempilhe()
    sentido2 = desempilha.dados

    return sentido1 == sentido2


main()
