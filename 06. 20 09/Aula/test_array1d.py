import pytest

from classes import array1d


@pytest.fixture()
def a():
    _a = array1d.Array1D([2, 3])
    return _a


def test_add(a):
    # array + float
    b = a + 1.5
    assert b.dados == [3.5, 4.5]

    # float + array
    d = 0.5 + a
    assert d.dados == [2.5, 3.5]

    # array + array
    d = a + b
    assert d.dados == [5.5, 7.5]

    # comutatividade
    e = b + a
    assert d.dados == e.dados

    # array + (-array)
    f = a + (-b)
    assert f.dados == [-1.5, -1.5]

    # comutatividade
    g = (-b) + a
    assert g.dados == f.dados


def test_sub(a):
    # array - float
    b = a - 1.5
    assert b.dados == [0.5, 1.5]

    # float - array
    d = 0.5 - a
    assert d.dados == [-1.5, -2.5]

    # array - array
    d = a - b
    assert d.dados == [1.5, 1.5]

    # comutatividade
    e = (-b) + a
    assert d.dados == e.dados

    # array - (-array)
    f = a - (-b)
    assert f.dados == [2.5, 4.5]

    # extra
    g = 2.5 - a
    assert g.dados == [0.5, -0.5]
