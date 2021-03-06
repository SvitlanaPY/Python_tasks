import unittest
from calc import Calc
from math import sqrt

class TestCalc(unittest.TestCase):
    """
    Тестування функцій в калькуляторі
    """

    def test_sum_001(self):
        self.assertEqual(Calc.sum(3, 7), 10)
        self.assertIsInstance(Calc.sum(3, 4.0), float)
        self.assertIsInstance(Calc.sum(4, 8), int)

    def test_minus_002(self):
        self.assertEqual(Calc.minus(30, 20), 10)
        with self.assertRaises(TypeError):
            Calc.minus(100, "60")
        self.assertIsInstance(Calc.minus(20.0, 5), float)

    def test_mul_003(self):
        self.assertIsInstance(Calc.mul(5, 6), int)
        self.assertEqual(Calc.mul(4, 10), 40)

        assert 24 in [11, 24, 32]

        self.assertIn(24, [11, 24, 32])
        self.assertIsInstance(Calc.mul(30.3, 4), float)

    def test_div_004(self):
        with self.assertRaises(ZeroDivisionError):
            Calc.div(10, 0)
        self.assertNotEqual(Calc.div(30, 3), 11)
        self.assertIsInstance(Calc.div(2, 2), float)

    def test_pow_005(self):
        self.assertNotIsInstance(Calc.pow(30.3, 4), int)
        self.assertEqual(Calc.pow(20, 2), 400)
        self.assertIsInstance(Calc.pow(20.1, 5), float)

    def test_sqrt_006(self):
        with self.assertRaises(TypeError):
            Calc.root("17", 50)
        self.assertNotEqual(Calc.root(21, 3), 20)
        self.assertIsInstance(Calc.root(3, 4), int)

    def test_per_from_number_007(self):
        self.assertEqual(Calc.perc(10, 100), 10)
        self.assertIsInstance(Calc.perc(30, 3), float)
        self.assertNotIsInstance(Calc.perc(10, 2), int)


if __name__ == '__main__':
    unittest.main()
