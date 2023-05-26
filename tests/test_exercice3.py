import pytest
import sys
from os.path import abspath, dirname

sys.path.insert(0, abspath(dirname(dirname(__file__))))

# Now you can import the Calculator class
# Add your test cases here
# tests/test_exercice3.py

from math import pi
from exercice3 import Shape, Rectangle, Circle, Square

def test_rectangle_area():
    rectangle = Rectangle(5, 10)
    assert rectangle.area() == 50

def test_rectangle_perimeter():
    rectangle = Rectangle(5, 10)
    assert rectangle.perimeter() == 30

def test_circle_area():
    circle = Circle(3)
    assert circle.area() == pi * 3 ** 2

def test_circle_perimeter():
    circle = Circle(3)
    assert circle.perimeter() == 2 * pi * 3

def test_square_area():
    square = Square(4)
    assert square.area() == 16

def test_square_perimeter():
    square = Square(4)
    assert square.perimeter() == 16

def test_square_inherits_from_rectangle():
    square = Square(4)
    assert isinstance(square, Rectangle)

def test_square_inherits_from_shape():
    square = Square(4)
    assert isinstance(square, Shape)
