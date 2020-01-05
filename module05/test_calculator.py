import unittest
import calculator

class CalculatorTestCase(unittest.TestCase):

    def test_add(self):
        assert calculator.add(4, 2) == 6

    def test_subtract(self):
        assert calculator.subtract(4, 2) == 2

    def test_multiply(self):
        assert calculator.multiply(4, 2) == 8

    def test_divide(self):
        assert calculator.divide(4, 2) == 2

if __name__ == "__main__":
    unittest.main()