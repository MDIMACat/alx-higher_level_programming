#!/usr/bin/python3
"""Class for Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class constructor"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize an instance of Square

        Args:
            size: Value for width and height of the square.
            x: Integer (optional) The x-axis for displaying the square.
            y: Integer (optional) The y-axis for displaying the square.
            id: Integer (optional) The ID of the square.
        """
        super().__init__(id=id, x=x, y=y, width=size, height=size)

    def __str__(self):
        """Returns a string representation"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self._x,
                self._y, self._width))

    @property
    def size(self):
        """Getter for size"""
        return self._width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigning new arguments to attributes"""
        attribute_names = ["id", "size", "x", "y"]

        if args:
            for name, value in zip(attribute_names, args):
                setattr(self, name, value)

        for name, value in kwargs.items():
            if name in attribute_names:
                setattr(self, name, value)
            else:
                raise ValueError("Invalid attribute {}".format(name))

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        sqr_dict = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
        return sqr_dict
