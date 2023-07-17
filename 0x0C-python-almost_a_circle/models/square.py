#!/usr/bin/python3

"""
Square class inherits from Rectangle class
get the Rectangle class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Update Rectangle"""
        variables = ['id', 'size', 'x', 'y']
        if args:
            for index, value in enumerate(args):
                if index < 4:
                    setattr(self, variables[index], value)
                else:
                    break
        elif kwargs:
            for key, value in kwargs.items():
                if key in variables:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ return a dictionatry """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
