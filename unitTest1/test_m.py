import unittest
from unitTest1 import mathLib


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_calc_add(self):
        res = mathLib.calc_add(5, 7)
        assert res == 12

    def test_calc_mul(self):
        res = mathLib.calc_mul(5, 5)
        assert res == 25

    def test_calc_sub(self):
        res = mathLib.calc_sub(5, 3)
        assert res == 2

    def test_calc_div(self):
        res = mathLib.calc_div(5, 2)
        assert res == 2.5


if __name__ == '__main__':
    unittest.main()
