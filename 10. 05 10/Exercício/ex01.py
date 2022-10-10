import numpy as np


def main():
    a = np.full((3, 4), 2)
    print(a.size)

    # a, e, h, j, l
    r = range(4 * 5)
    b = np.array(r).reshape(5, 4)
    print(b[1][3], b[1, 3])
    print(b[1:][3], b[1:, 3])

    print()

    print(b[1:][:3], '\n', b[1:, :3])

    c = b[1:, :3]
    print(c.shape)
    b[2, 2] = 0
    print(c)  # vista

    c = b[:]
    print()
    print(b)
    b[2, 2] = 0
    print(c)

    c = b[:, :]
    print()
    print(b)
    b[2, 2] = 0
    print(c)

    c = b[:][:]
    print()
    print(b)
    b[2, 2] = 0
    print(c)


main()
