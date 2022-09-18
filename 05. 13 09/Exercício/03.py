from classes.stack import Pilha


def main():
    print(pal([11, [True, None], 11]))


def pal(s):
    p = Pilha()
    for i in range(len(s)):
        p.empilhe(s[i])
    for i in range(len(s)):
        if s[i] != p.desempilhe():
            return False
    return True


main()
