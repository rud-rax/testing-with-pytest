

import pytest
import math
from src.classBasedTesting.Shape.shapes import *

class TestSquare():

    def setup_method(self) :

        print('Setting up class Square')
        self.shape = Square(5)

    def teardown_method(self) :

        print('Tearing down class Square ')
        del self.shape

    def test_area(self) :

        print('Testing area of shape')
        assert self.shape.area() == self.shape.side ** 2

    def test_perimeter(self) :

        print('Testing perimeter of shape')
        result = self.shape.perimeter()
        expected = self.shape.side * 4
        assert result == expected

class TestCircle() :

    def setup_method(self) :

        print('Setting up class Circle')
        self.shape = Circle(5)

    def teardown_method(self) :

        print('Tearing down class Circle ')
        del self.shape

    def test_area(self) :

        print('Testing area of circle')
        assert self.shape.area() == math.pi * self.shape.radius ** 2

    def test_perimeter(self) :

        print('Testing perimeter of circle')
        result = self.shape.perimeter()
        expected = self.shape.radius * 2 * math.pi
        assert result == expected


class TestRectangle:

    def setup_method(self, method):
        self.rect = Rectangle(10, 5)
        print(f"Setup {method.__name__}")

    def teardown_method(self, method):
        print(f"Teardown {method.__name__}")

    def test_rectangle_area(self):
        rect = Rectangle(10, 5)
        assert rect.area() == 50, "Area should be length multiplied by breadth"

    def test_rectangle_perimeter(self):
        rect = Rectangle(10, 5)
        assert rect.perimeter() == 30, "Perimeter should be twice the sum of length and breadth"

    def test_rectangle_area_with_zero(self):
        rect = Rectangle(0, 5)
        assert rect.area() == 0, "Area should be zero when one side is zero"

    def test_rectangle_perimeter_with_zero(self):
        rect = Rectangle(0, 5)
        assert rect.perimeter() == 10, "Perimeter should be twice the breadth when length is zero"

    def test_rectangle_negative_sides(self):
        with pytest.raises(ValueError):
            Rectangle(-10, 5)
