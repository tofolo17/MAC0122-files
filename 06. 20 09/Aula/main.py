from classes.array1d import Array1D
from classes.array2d import Array2D


def testes_array1d():
    x = Array1D([2, 3])
    y = x + 1.5
    print(f"{y} deve ser [3.5, 4.5]")

    y = 2 + x
    print(f"{y} deve ser [4, 5]")


def testes_array2d():
    a = Array2D((2, 3), 3)
    b = Array2D((2, 3), 1.7)
    c = a + b
    d = a - b
    e = 2 + a
    f = b + 2
    g = 2.5 - a
    h = b - 2.5
    print(f"a+b   = {c}")
    print(f"a-b   = {d}")
    print(f"2+a   = {e}")
    print(f"b+2   = {f}")
    print(f"2.5-a = {g}")
    print(f"b-2.5 = {h}")


if __name__ == '__main__':
    testes_array1d()
    testes_array2d()
