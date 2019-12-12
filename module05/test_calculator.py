import pytest
import unittest
import calculator

'''
class Prequels(unittest.TestCase):

    def setUp(self):
        self.test_calc = calculator
        # print("    setUp executes before every test method!")

    def tearDown(self):
        print("    tearDown executes after every test method!")
'''
#class CalculatorTestCase(Prequels):
class CalculatorTestCase(unittest.TestCase):
    
    def setUp(self):
        self.test_calc = calculator.Calculator()

    def test_add(self):
        self.add_result = self.test_calc.add(4, 2)
        assert self.add_result == 6, 'Test failed.'

    def test_subtract(self):
        self.add_result = self.test_calc.subtract(4, 2)
        assert self.add_result == 2, 'Test failed.'

    def test_multiply(self):
        self.add_result = self.test_calc.multiply(4, 2)
        assert self.add_result == 8, 'Test failed.'

    def test_divide(self):
        self.add_result = self.test_calc.divide(4, 2)
        assert self.add_result == 2, 'Test failed.'