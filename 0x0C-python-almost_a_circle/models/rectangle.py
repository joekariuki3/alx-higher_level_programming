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
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 1:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 1:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ return the area of a Rectangle"""
        return self.width * self.height

    def display(self):
        """prints the shape of a rectangle"""
        if self.y != 0:
            print("\n" * (self.y - 1))
        for row in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """print object"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".
                format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """Update Rectangle"""
        variables = ['id', 'width', 'height', 'x', 'y']
        if args:
            for index, value in enumerate(args):
                if index < 5:
                    setattr(self, variables[index], value)
                else:
                    break
        elif kwargs:
            for key, value in kwargs.items():
                if key in variables:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ return a dictionatry """
        return {'id': self.id, 'width': self.width, 'height': self.
                height, 'x': self.x, 'y': self.y}
