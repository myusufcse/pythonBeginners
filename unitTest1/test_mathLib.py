import unittest
from unitTest1 import mathLib


def test_calc_add():
    res = mathLib.calc_add(5, 7)
    assert res == 12


def test_calc_mul():
    res = mathLib.calc_mul(5, 5)
    assert res == 25


def test_calc_sub():
    res = mathLib.calc_sub(5, 3)
    assert res == 2


def test_calc_div():
    res = mathLib.calc_div(5, 2)
    assert res == 2.5


if __name__ == '__main__':
    unittest.main()
