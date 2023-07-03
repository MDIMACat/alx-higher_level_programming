#!/usr/bin/python3
"""Define a rectangle"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """ Initialize a rectangle

        Args: width (int) width of rectangle
            height (int) height of rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Get the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Get the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """String representation"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += "#" * self.__width + "\n"
        return rectangle_str.rstrip()

    def __repr__(self):
        """Remove represenstation"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
