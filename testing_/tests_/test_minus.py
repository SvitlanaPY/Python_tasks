import unittest
from calc import Calc

class TestMinus(unittest.TestCase):
    """
    TESTing_ subtraction of values in calculator
    """
    def setUp(self) -> None:
        print('setUp')

    def test_Subtract_DataInputs(self):
        print('test_Subtract_DataInputs')
        self.assertIsInstance(Calc.minus(1, 2), int)
        self.assertIsInstance(Calc.minus(2.0, 2), float)
        self.assertIsInstance(Calc.minus(2, 3.0), float)

    def test_Subtract_Computing(self):
        print('test_Subtract_Computing')
        self.assertEqual(Calc.minus(0.0, 0), 0)
        self.assertEqual(Calc.minus(-5, -5), 0.0)
        self.assertEqual(Calc.minus(-5, 2), -7)
        self.assertEqual(Calc.minus(10, 5.0), 5)

    def test_Subtract_RaiseExceptions(self):
        print('test_Subtract_RaiseExceptions')
        # self.assertRaises(TypeError, Calc.minus, 52, "2")
        with self.assertRaises(TypeError):
            Calc.minus(52, "2")

    def tearDown(self) -> None:
        print('tearDown\n')


if __name__ == '__main__':
    unittest.main()
