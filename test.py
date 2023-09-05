from functions import divide
from functions import add
from functions import multiply


def test_divide():
    assert 2 == divide(4, 2)


def test_add():
    assert 4 == add(2, 2)


def test_multiply():
    assert 4 == multiply(2, 2)