import unittest
from calculator import add
from calculator import subtract
from calculator import multiply
from calculator import divide

class CalculatorTestCase(unittest.TestCase):

    def test_add(self):
        assert add(4, 2) == 6

    def test_subtract(self):
        assert subtract(4, 2) == 2

    def test_multiply(self):
        assert multiply(4, 2) == 8

    def test_divide(self):
        assert divide(4, 2) == 2

if __name__ == "__main__":
    unittest.main()