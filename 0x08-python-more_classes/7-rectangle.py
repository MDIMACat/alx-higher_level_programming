#!/usr/bin/python3
"""
Object for rectangle
"""


class Rectangle:
    """
    This is a class that implements a basic rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        answer = self._width * self._height
        return answer

    def perimeter(self):
        if self._width == 0 or self._height == 0:
            return 0
        answer = 2 * (self._height + self._width)
        return answer

    def __str__(self):
        if self._width == 0 or self._height == 0:
            return ""

        result = ""
        for _ in range(self._height):
            result += Rectangle.print_symbol * self._width + "\n"
        return result.rstrip()

    def __repr__(self):
        return "Rectangle({}, {})".format(self._width, self._height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
