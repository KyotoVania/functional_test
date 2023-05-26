import pytest

# Add your test cases here
# tests/test_exercice1.py

from exercice1 import Calculator

def test_calculator_add():
    calculator = Calculator()
    result = calculator.add(2, 3)
    assert result == 5
    assert calculator.get_memory() == 5

def test_calculator_subtract():
    calculator = Calculator()
    result = calculator.subtract(5, 2)
    assert result == 3
    assert calculator.get_memory() == 3

def test_calculator_multiply():
    calculator = Calculator()
    result = calculator.multiply(4, 3)
    assert result == 12
    assert calculator.get_memory() == 12

def test_calculator_divide():
    calculator = Calculator()
    result = calculator.divide(10, 2)
    assert result == 5
    assert calculator.get_memory() == 5

def test_calculator_power():
    calculator = Calculator()
    result = calculator.power(2, 3)
    assert result == 8
    assert calculator.get_memory() == 8

def test_calculator_sqrt():
    calculator = Calculator()
    result = calculator.sqrt(16)
    assert result == 4
    assert calculator.get_memory() == 4

def test_calculator_clear_memory():
    calculator = Calculator()
    calculator.add(2, 3)
    calculator.clear_memory()
    assert calculator.get_memory() == 0
