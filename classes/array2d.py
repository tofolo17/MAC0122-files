class Array2D:
    def __init__(self, shape: tuple, val):
        self.shape = shape
        self.size = self.shape[0] * self.shape[1]
        self.data = [val] * self.size

    def reshape(self, shape):
        a = Array2D(shape, 0)
        a.data = self.data

        return a

    def copy(self):
        a = Array2D(self.shape, 0)
        a.data = self.data[:]

        return a

    def __getitem__(self, key):
        return self.data[self.shape[1] * key[0] + key[1]]

    def __setitem__(self, key, valor):
        self.data[self.shape[1] * key[0] + key[1]] = valor

    def __str__(self):
        s = ""
        for i in range(1, self.size + 1):
            if i % self.shape[1] == 0:
                s += f'{self.data[i - 1]} \n'
            else:
                s += f'{self.data[i - 1]} '

        return s

    def __add__(self, other):
        # Assume Array2D's de mesmo shape
        res = Array2D(self.shape, 0)
        for i in range(len(self.data)):
            if type(other) == int or type(other) == float:
                res.data[i] = self.data[i] + other
            else:
                res.data[i] = self.data[i] + other.data[i]
        return res

    def __sub__(self, other):
        # Assume Array2D's de mesmo shape
        res = Array2D(self.shape, 0)
        for i in range(len(self.data)):
            if type(other) == int or type(other) == float:
                res.data[i] = self.data[i] - other
            else:
                res.data[i] = self.data[i] - other.data[i]
        return res

    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        return -(self - other)

    def __neg__(self):
        res = Array2D(self.shape, 0)
        for i in range(len(self.data)):
            res.data[i] = -self.data[i]
        return res
