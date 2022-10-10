I = 'abc'
F = 'xyz'


def main():
    print(f"a) {_02('a b y x c z')}\n")
    print(f"b) {_02('aa b yxx a x c z')}\n")
    print(f"c) {_02('( c a ) x z')}\n")
    print(f"d) {_02('c a a b x y x z')}\n")
    print(f"e) {_02('a c a x c a b y x z z x')}\n")
    print(f"f) {_02('a a x x x a x a')}\n")
    print(f"g) {_02('c b y z a x x a')}\n")
    print(f"h) {_02('a x x a')}\n")
    print(f"i) {_02('[’a’, ’b’, ’y’, ’c’, ’a’, ’x’, ’z’, ’c’, ’b’, ’y’, ’z’, ’-1’, ’x’]')}\n")


def _02(s):
    p = []
    for c in s:
        if c in I:
            p.append(c)
        elif c in F:
            if not p:
                print('Linha 8')
                return False
            t = p.pop()
            if I.index(t) != F.index(c):
                print('Linha Pré-aula')
                return False
    return p == []


main()

# a, d, e, h
