import pytest
import unittest
import calculator

class MyTestClass(unittest.TestCase):
    
    def setUp(self):
        self.test_calc = calculator()

    def test_add_true(self):
        self.x = 3
        self.y = 4
        self.calculator_add = self.test_calc.add(self.x, self.y)
        assert (self.x + self.y) == self.calculator_add, 'Test failed.'