import pytest
from calculator import add

def test_add():
    result = add(2, 3)
    assert result == 5
def test_add_zero():
    result = add(7, 0)
    assert result == 7
def test_add_negative():
    result = add(-4, 1)
    assert result == -3