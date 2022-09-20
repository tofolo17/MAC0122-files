import pytest

from classes.array2d import Array2D


@pytest.fixture
def a():
    _a = Array2D((2, 3), 3)
    return _a


@pytest.fixture
def b():
    _b = Array2D((2, 3), 1.7)
    return _b


def test_add(a, b):
    size = a.size

    c = a + b
    d = a - b
    e = 2 + a
    f = b + 2
    g = 2.5 - a
    h = b - 2.5

    assert c.data == [3 + 1.7] * size
    assert d.data == [3 - 1.7] * size
    assert e.data == [2 + 3] * size
    assert f.data == [1.7 + 2] * size

    # float - array2d
    assert g.data == [2.5 - 3] * size

    assert h.data == [1.7 - 2.5] * size
