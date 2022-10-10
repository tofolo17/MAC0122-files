import numpy as np

lisa = [[1, 2, 3], [4, 5, 6]]
bart = np.array(lisa)
simp = np.array([[7, 8, 9], [10, 11, 12]])

# comandos
simp = bart[:]
bart[1, 1] = 0
print(simp)

# f, h, j, k, l
