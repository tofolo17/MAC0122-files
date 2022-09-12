from stack import Pilha


def main():
    s = "(([[]]))"
    print(bem_formada(s))


def bem_formada(s):
    p = Pilha()
    for char in s:
        if char == '(':
            p.empilhe(char)
        if char == ')' and not p.vazia():
            if p.topo() == '(':
                p.desempilhe()

        if char == '[':
            p.empilhe(char)
        if char == ']' and not p.vazia():
            if p.topo() == '[':
                p.desempilhe()

    return p.vazia()


main()
