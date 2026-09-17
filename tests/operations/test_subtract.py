import pytest
from calculator import subtract

def test_subtract():
    result = subtract(5, 3)
    assert result == 2
def test_subtract_negative_result():
    result = subtract(3, 5)
    assert result == -2

def test_subtract_zero():
    result = subtract(7, 0)
    assert result == 7
    
