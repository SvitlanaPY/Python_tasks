import unittest
from testing_.calc import Calc


class TestDiv(unittest.TestCase):
    """
    TESTing_ division of values in calculator
    """
    def setUp(self) -> None:
        print('setUp')

    def test_Divide_DataInputs(self):
        print('test_Divide_DataInputs')
        self.assertIsInstance(Calc.div(4, 2), float)
        self.assertIsInstance(Calc.div(2.0, 2), float)
        self.assertIsInstance(Calc.div(50, 2.0), float)

    def test_Divide_Computing(self):
        print('test_Divide_Computing')
        self.assertEqual(Calc.mul(0.0, 1), 0)
        self.assertEqual(Calc.div(100, 2.0), 50)
        self.assertEqual(Calc.div(-50, 2), -25)
        self.assertEqual(Calc.div(-5, -5), 1.0)

    def test_Division_RaiseExceptions(self):
        print('test_Division_RaiseExceptions')
        # self.assertRaises(ZeroDivisionError, Calc.div, 10, 0)
        with self.assertRaises(ZeroDivisionError):
            Calc.div(10, 0)
        # self.assertRaises(TypeError, Calc.div, 52, "2")
        with self.assertRaises(TypeError):
            Calc.div(52, "2")

    def tearDown(self) -> None:
        print('tearDown\n')


if __name__ == '__main__':
    unittest.main()
