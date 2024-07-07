import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculate = Calculator()
    
    def test_addition(self):
        self.calculate.input('5')
        self.calculate.input('+')
        self.calculate.input('3')
        self.calculate.input('=')
        self.assertEqual(self.calculate.get_current_value(), '8')
    

    def test_subtraction(self):
        self.calculate.input('10')
        self.calculate.input('-')
        self.calculate.input('4')
        self.calculate.input('=')
        self.assertEqual(self.calculate.get_current_value(), '6')
    

    def test_multiplication(self):
        self.calculate.input('6')
        self.calculate.input('*')
        self.calculate.input('7')
        self.calculate.input('=')
        self.assertEqual(self.calculate.get_current_value(), '42')

    def test_parentheses(self):
        self.calculate.input('(')
        self.calculate.input('4')
        self.calculate.input('+')
        self.calculate.input('6')
        self.calculate.input(')')
        self.calculate.input('*')
        self.calculate.input('2')
        self.calculate.input('=')
        self.assertEqual(self.calculate.get_current_value(), '20')

    def test_clear(self):
        self.calculate.input('5')
        self.calculate.input('+')
        self.calculate.input('3')
        self.calculate.input('C')
        self.assertEqual(self.calculate.get_current_value(), '')

    def test_unmatched_parentheses(self):
        self.calculate.input('(')
        self.calculate.input('3')
        self.calculate.input('+')
        self.calculate.input('4')
        self.calculate.input('=')
        self.assertEqual(self.calculate.get_current_value(), '7')


if __name__ == '__main__':
    unittest.main()