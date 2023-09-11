#!/usr/bin/python3
"""
Defines the Rectangle classes
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Implementation for Rectangle
    """
    def __init__(self, width, height):
        """
        Instantiates a Rectangle with a given width and height.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Computes the area of the rectangle.
        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        Returns:
            str: A string in the format "[Rectangle] <width>/<height>"
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
