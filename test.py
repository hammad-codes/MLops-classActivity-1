from functions import add
from functions import multiply
from functions import divide
def test_add():
    assert 4 == add(2,2)
    
def test_multiply():
    assert 4 == multiply(2,2)
    
def test_divide():
    assert 1 == divide(2,2)    