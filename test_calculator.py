"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)

    def test_division(self):
        assert 500 == calculator.divide(25000, 50)

    def test_squareroot(self):
        assert 5 == calculator.square_root(25)

    def test_is_negative(self):
        assert True is calculator.is_negative(-5)
        assert False is calculator.is_negative(5)

    def test_is_positive(self):
        assert True is calculator.is_positive(5)
        assert False is calculator.is_positive(-5)

    
