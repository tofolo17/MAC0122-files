from ex00 import *
from ex01 import *


def test_pal():
    s = "ovo"
    assert pal(s) is True

    s = "ovelha"
    assert pal(s) is False

    s = "luz azul"
    assert pal(s) is True


def test_pal_internet():
    s = "ovo"
    assert pal_internet(s) is True

    s = "ovelha"
    assert pal_internet(s) is False

    s = "luz azul"
    assert pal_internet(s) is True


def test_bem_formada():
    s = '(([]))'
    assert bem_formada(s) is True

    s = '['
    assert bem_formada(s) is False

    s = '))'
    assert bem_formada(s) is True

    s = '()['
    assert bem_formada(s) is False

    s = '[][()]()'
    assert bem_formada(s) is True
