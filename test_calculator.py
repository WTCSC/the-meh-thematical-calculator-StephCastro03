import pytest
from Meh_Calculator import add, subtract, multiply, divide
def test_add_positive_numbers():
    assert add(5,3) == 8
def test_add_negative_numbers():
    assert add(-4,-6) == -10
def test_subtract_postive_numbers():
    assert subtract(10, 4) == 6
def test_subtract_larger_from_smaller():
    assert subtract(4, 10) == -6
def test_multiply_positive_numbers():
    assert multiply(5, 6) == 30
def test_multiply_by_zero():
    assert multiply(7,0) == 0
def test_divide_positive_numbers():
    assert divide(8, 2) == 4
def test_divide_by_one():
    assert divide(9, 1) == 9
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)