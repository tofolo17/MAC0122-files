import pytest

from classes.array2d import Array2D

# Parâmetros
ARRAY_CONFIG = [
    [(3, 3), 3],
    [(2, 3), 1.7]
]

# Valores esperados
SIZE = [9, 6]
DATA = [[3, 3, 3, 3, 3, 3, 3, 3, 3], [1.7, 1.7, 1.7, 1.7, 1.7, 1.7]]


def combine():
    for arr, size, data in zip(ARRAY_CONFIG, SIZE, DATA):
        yield Array2D(*arr), size, data


@pytest.mark.parametrize('array, size, data', combine())
def test_size_and_data(array, size, data):
    assert array.size == size
    assert array.data == data
