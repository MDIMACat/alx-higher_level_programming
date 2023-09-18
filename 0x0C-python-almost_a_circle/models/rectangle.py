#!/usr/bin/python3
"""Class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Class constructor"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize an instance of rectangle

        Args:
        width : integer
            The width for the rectangle
        height : integer
            The height for the rectangle
        x : integer (optional)
            The x axis for displaying the rectangle
        y : interger(optional)
            The y axis for displaying the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def check_attribute(self, name, value):
        """
        checks the given attribute.

        ArgsL
        name : string
            The name for the instance attribute to validate
        value : integer
            The value for the instance attribute

        Raises
        TypeError
            When the given value is not an integer
        ValueError
            When the value given is 0 or less and the name
            is width or height. And also when the given
            value is a negative value and the name is x or y.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if (name in ["width", "height"]):
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        elif (name in ["x", "y"]):
            if value < 0:
                raise ValueError("{} must be >= 0". format(name))

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self.check_attribute("width", value)
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self.check_attribute("height", value)
        self._height = value

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self.check_attribute("x", value)
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self.check_attribute("y", value)
        self._y = value

    def area(self):
        """Method to calculate area"""
        return self._width * self._height

    def display(self):
        """ prints in stdout the Rectangle instance with the character #"""
        result = ""
        for _ in range(self._y):
            result += "\n"
        for _ in range(self._height):
            result += " " * self._x + "#" * self._width + "\n"
        print(result.rstrip())

    def update(self, *args, **kwargs):
        """Assigning new arguments to attributes"""
        attributes_name = ["id", "width", "height", "x", "y"]

        if args:
            for name, value in zip(attributes_name, args):
                setattr(self, name, value)

        for name, value in kwargs.items():
            if name in attributes_name:
                setattr(self, name, value)
            else:
                raise ValueError("Invalid attribute: {}". format(name))

    def __str__(self):
        """Returns a string representation"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self._x,
                self._y, self._width, self._height))

    def to_dictionary(self):
        """Returns the dictionary representation"""
        rect_dict = {
           "id": self.id,
           "width": self.width,
           "height": self.height,
           "x": self.x,
           "y": self.y
        }
        return rect_dict
