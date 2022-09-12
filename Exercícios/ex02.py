class Fraction:
    def __init__(self, cima, baixo):
        self.num = cima
        self.den = baixo

    def __str__(self):
        return f"{self.num}/{self.den}"

    def show(self):
        print(f"{self.num}/{self.den}")

    def add(self, other):
        novonum = self.num * other.den + self.den * other.num
        novoden = self.den * other.den
        return Fraction(novonum, novoden)


# b, d, f, g, h, j, l, n, p


def HFmaior(n):
    """ (int) -> Fraction
    RECEBE um inteiro positivo n.
    RETORNA o valor de 1 + 1/2 + ... + 1/n
    """
    hn = Fraction(0, 1)  # LACUNA 1
    for i in range(1, n + 1):
        f = Fraction(1, i)  # LACUNA 2
        hn = hn.add(f)  # LACUNA 3
    return hn


def Hmenor(n):
    """ (int) -> float
    RECEBE um inteiro positivo n.
    RETORNA o valor de 1/n + 1/(n-1) + ... + 1/2 + 1
    """
    hn = 0  # LACUNA 4
    i = n
    while i > 0:
        f = 1 / i  # LACUNA 5
        hn += f
        i -= 1
    return hn


print(HFmaior(3), Hmenor(3))
