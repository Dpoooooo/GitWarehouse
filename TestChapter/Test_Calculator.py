# 计算机自动化测试

import pytest

from Calculator import Calculator

def test_add_positive():
    calc = Calculator()
    assert calc.add(1, 2) == 3

def test_add_negative():
    calc = Calculator()
    assert calc.add(-1, -2) == -3

def test_mul_every():
    calc = Calculator()
    assert calc.mul(2, 2) == 4

def test_div_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.div(10, 0)

def test_div_every():
    calc = Calculator()
    assert calc.div(10, 2) == 5
