class Array1D:
    def __init__(self, d):
        if type(d) is int:
            self.dados = d * [0]
            return
        if type(d) == list:
            n = len(d)
            self.dados = n * [0]
            for i in range(n):
                self.dados[i] = d[i]

    def __str__(self):
        s = f'{self.dados}'
        return s

    def __add__(self, other):
        # Assume Array1D's de mesmo tamanho
        n = len(self.dados)
        res = Array1D(n)
        for i in range(n):
            if type(other) == int or type(other) == float:
                res.dados[i] = self.dados[i] + other
            else:
                res.dados[i] = self.dados[i] + other.dados[i]
        return res

    def __sub__(self, other):
        n = len(self.dados)
        res = Array1D(n)
        for i in range(n):
            if type(other) == int or type(other) == float:
                res.dados[i] = self.dados[i] - other
            else:
                res.dados[i] = self.dados[i] - other.dados[i]
        return res

    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        return - (self - other)

    def __neg__(self):
        n = len(self.dados)
        res = Array1D(self.dados)
        for i in range(n):
            res.dados[i] = -self.dados[i]
        return res
