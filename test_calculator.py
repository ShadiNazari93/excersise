# from check import *
# print(div(2,3))
# print(mul(2,3))
# print(add(2,3))
# print(sub(2,3))

#########################################################
# pip install pytest
import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(0, 3) == -3

def test_multiply():
    assert multiply(2, 4) == 8
    assert multiply(-2, 3) == -6

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3

def test_divide_by_zero():
    with pytest.raises(ValueError) as e:
        divide(5, 0)
    assert str(e.value) == "تقسیم بر صفر مجاز نیست!"

#pytest test_calculator.py