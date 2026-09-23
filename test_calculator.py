import pytest
from calculator import add, divide

from calculator import substract, multiply

def test_add():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, 1) == 0
def test_divide():
    assert divide(10, 2) == 5

def test_substract():
    assert substract(5, 3) == 2

def test_substract_negative():
    assert substract(-1, 3) == -4

def test_substract_zero():
    assert substract(0, 5) == -5

def test_multiply():
    assert multiply(2, 3) == 6

def test_multiply_negative():
    assert multiply(3, -4) == -12

def test_multiply_zero():
    assert multiply(3, 0) == 0

def test_divide_by_zero():
    with pytest.raises(ValueError):
