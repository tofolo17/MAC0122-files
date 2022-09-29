def main():
    pol = [1.1, 1.6, '-', 3, '+']  # Os valores da lista eram strings ou floats?

    print(calcule(pol))


def calcule(polonesa):
    p = []
    ops = ['+', '-', '*', '/']
    for char in polonesa:
        if char not in ops:
            p.append(char)
        else:
            b = p.pop()
            a = p.pop()
            r = 0

            if char == '+':
                r = a + b
            if char == '-':
                r = a - b
            if char == '*':
                r = a * b
            if char == '/':
                r = a // b

            p.append(r)
    return float(p[0])


main()
