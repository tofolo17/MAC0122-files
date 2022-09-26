from classes.array2d import Array2D


def test_reshape():
    a = Array2D((1, 6), 3)
    assert a.data == [3] * 6

    b = a.reshape((2, 3))
    assert b.data == [3] * 6

    b[1, 2] = 10
    assert b.data == a.data

    a[0, 2] = -1
    assert a.data == b.data

    a = Array2D((1, 6), 3)
    c = a.copy()
    assert a.data == c.data

    a[0, 1] = 99
    c[0, 5] = -1
    assert a.data != c.data


test_reshape()
