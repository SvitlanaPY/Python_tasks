import unittest
from calc import Calc


class TestPerc(unittest.TestCase):
    """
    TESTing_ percentage of any number in calculator
    """
    def setUp(self) -> None:
        print('setUp')

    def test_Percentage_DataInputs(self):
        print('test_Percentage_DataInputs')
        self.assertIsInstance(Calc.perc(1, 2), float)
        self.assertIsInstance(Calc.perc(2.0, 2), float)
        self.assertIsInstance(Calc.perc(2, 3.0), float)

    def test_Percentage_Computing(self):
        print('test_Percentage_Computing')
        self.assertEqual(Calc.perc(0.0, 0), 0)
        self.assertEqual(Calc.perc(35, 500), 175.0)
        self.assertEqual(Calc.perc(10, 100.0), 10)

    def test_Percentage_SpecialCase(self):
        print('test_Percentage_RaiseExceptions')
        with self.assertRaises(TypeError):
            Calc.perc("10", 100)

    def tearDown(self) -> None:
        print('tearDown\n')


if __name__ == '__main__':
    unittest.main()
