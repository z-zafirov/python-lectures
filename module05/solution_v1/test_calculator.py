#import pytest
import unittest
import calculator

class CalculatorTestCase(unittest.TestCase):

    def setUp(self):
        self.test_calc = calculator.Calculator()

    def test_add(self):
        self.result = self.test_calc.add(4, 2)
        assert self.result == 6, 'Test failed.'

    def test_subtract(self):
        self.result = self.test_calc.subtract(4, 2)
        assert self.result == 2, 'Test failed.'

    def test_multiply(self):
        self.result = self.test_calc.multiply(4, 2)
        assert self.result == 8, 'Test failed.'

    def test_divide(self):
        self.result = self.test_calc.divide(4, 2)
        assert self.result == 2, 'Test failed.'

if __name__ == "__main__":
    unittest.main()