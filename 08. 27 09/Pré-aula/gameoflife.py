import numpy as np


def main():
    size = l, c = 4, 4
    init_state = np.zeros(size, dtype=np.int8)

    # Alterando condição inicial
    init_state[0, 0] = 1
    init_state[0, 1] = 1
    init_state[1, 2] = 1

    # Criando uma cópia para alterações
    final_state = init_state.copy()

    print(init_state)
    print()

    for i in range(l):
        for j in range(c):
            cell = init_state[i, j]

            if i == 0:
                slice_01 = init_state[0:2]
            else:
                slice_01 = init_state[i - 1:i + 2]
            if j == 0:
                slice_02 = slice_01[:, 0:2]
            else:
                slice_02 = slice_01[:, j - 1:j + 2]
            s = slice_02.sum() - cell

            if cell == 0 and s == 3:
                final_state[i][j] = 1
            if cell == 1 and s not in [2, 3]:
                final_state[i][j] = 0

    print(final_state)


main()
