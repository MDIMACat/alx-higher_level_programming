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
        obj_str = ""

        if (self._width == 0 or self._height == 0):
            return (obj_str)
        for row in range(0, self._height, 1):
            for col in range(0, self._width, 1):
                obj_str += str(self.print_symbol)
            if ((row == self._height - 1) and (col == self._width - 1)):
                break
            obj_str += "\n"

        return (obj_str)

    def __repr__(self):
        return "Rectangle({}, {})".format(self._width, self._height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if (type(rect_1) is Rectangle):
            if (type(rect_2) is Rectangle):
                if (rect_1.area() >= rect_2.area()):
                    return rect_1
                return rect_2
            else:
                raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            raise TypeError("rect_1 must be an instance of Rectangle")
