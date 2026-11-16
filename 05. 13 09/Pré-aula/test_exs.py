import sys
from pathlib import Path

# Permite importar os módulos vizinhos (ex00, ex01) no pytest
sys.path.insert(0, str(Path(__file__).resolve().parent))

from ex00 import *  # noqa: E402, F403
from ex01 import *  # noqa: E402, F403


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
