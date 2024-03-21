
from abc import ABC , abstractmethod
import math

class Shape() :


    def area() :
        pass


    def perimeter():
        pass

class Circle(Shape) :

    def __init__(self , radius) -> None:
        super().__init__()

        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return math.pi * self.radius * 2

class Square(Shape) :

    def __init__(self , side) -> None:
        super().__init__()
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self) :
        return self.side * 4


class Rectangle():
    def __init__(self, length , breadth) -> None:

        if length < 0 or breadth < 0 :
            raise ValueError

        self.length = length
        self.breadth = breadth

    def area(self) :
        return self.length * self.breadth

    def perimeter(self) :
        return (self.breadth + self.length) * 2
