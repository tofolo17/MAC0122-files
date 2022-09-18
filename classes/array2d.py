class Array2D:
    def __init__(self, shape: tuple, val):
        self.shape = shape
        self.size = self.shape[0] * self.shape[1]
        self.data = [val] * self.size

    # ---------------------------------------------------------------
    def __getitem__(self, key):
        return self.data[self.shape[1] * key[0] + key[1]]

    # ---------------------------------------------------------------
    def __setitem__(self, key, valor):
        self.data[self.shape[1] * key[0] + key[1]] = valor

    # ---------------------------------------------------------------
    def __str__(self):
        s = ""
        for i in range(1, self.size + 1):
            if i % self.shape[1] == 0:
                s += f'{self.data[i - 1]} \n'
            else:
                s += f'{self.data[i - 1]} '

        return s


my_array = Array2D((2, 3), 3)
print(my_array)
