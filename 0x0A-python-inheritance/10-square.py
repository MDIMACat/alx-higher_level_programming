#!/usr/bin/python3
"""Square Classs"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Implementing a square class"""
    def __init__(self, size):
        """
        Instantiates a Rectangle with a given size
        Args:
            size (int)
        """
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def area(self):
        """
        Computes the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
