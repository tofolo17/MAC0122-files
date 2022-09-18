import pytest

from classes.array2d import Array2D

ARRAY_CONFIG = [
    [(2, 3), 3],
    [(2, 3), 1.7]
]
SIZE = [6, 6]
DATA = [
    [3, 3, 3, 3, 3, 3],
    [1.7, 1.7, 1.7, 1.7, 1.7, 1.7]
]


def combine(list1, list2):
    return [(list1[i], list2[i]) for i in range(len(list1))]


# Without pytest decorators --> look's better
def test_size_and_data():
    for i in range(len(ARRAY_CONFIG)):
        array_config = ARRAY_CONFIG[i]
        size = SIZE[i]
        data = DATA[i]

        array = Array2D(*array_config)
        assert array.size == size
        assert array.data == data


# With decorators, but maybe not ideally
@pytest.fixture
def array(request):
    return Array2D(*request.param)


# Should this really be that repetitive?
@pytest.mark.parametrize('array, expected', combine(ARRAY_CONFIG, SIZE), indirect=['array'])
def test_size(array, expected):
    assert array.size == expected


@pytest.mark.parametrize('array, expected', combine(ARRAY_CONFIG, DATA), indirect=['array'])
def test_data(array, expected):
    assert array.data == expected


# Other tests --> generate 4 tests instead of 2
@pytest.fixture(params=ARRAY_CONFIG)
def array(request):
    return Array2D(*request.param)


@pytest.fixture
def array_size(array):
    return array.size


@pytest.mark.parametrize('expected', SIZE)
def test_size(array_size, expected):
    assert array_size == expected
