import unittest
from calc import Calc


class TestSum(unittest.TestCase):
    """
    TESTing_ adding of values in calculator
    """

    def setUp(self) -> None:
        print('setUp')

    def test_Add_DataInputs(self):
        print('test_Add_DataInputs')
        self.assertIsInstance(Calc.sum(1, 2), int)
        self.assertIsInstance(Calc.sum(2.0, 2), float)
        self.assertIsInstance(Calc.sum(2, 3.0), float)

    def test_Add_Computing(self):
        print('test_Add_Computing')
        self.assertEqual(Calc.sum(0.0, 0), 0)
        self.assertEqual(Calc.sum(3, 3), 6.0)
        self.assertEqual(Calc.sum(-5, 2), -3)
        self.assertEqual(Calc.sum(105, 5.0), 110)

    def test_Add_RaiseExceptions(self):
        print('test_Add_RaiseExceptions')
        # self.assertRaises(TypeError, Calc.sum, "1", 2)
        with self.assertRaises(TypeError):
            Calc.sum("1", 2)

    def tearDown(self) -> None:
        print('tearDown\n')


if __name__ == '__main__':
    unittest.main()

# if there is unittest.main() in a python-file then run command ~$ python3 HW#11_UnitTests.py
# or
# if there is no unittest.main() in a python-file,
# then run command ~$ python3 -m unittest -v HW#11_UnitTests.py > output_unittesting.txt
# testing_unittesting results will be saved in file 'output_unittesting.txt'
