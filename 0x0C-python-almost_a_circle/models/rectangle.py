#!/usr/bin/python3

"""
Rectangle class inherits from Base class
get the base class
"""


from models.base import Base


class Rectangle(Base):
    """
    initiate the class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__()
        self.id = id
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def x(self):
        return self._x

    @width.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
