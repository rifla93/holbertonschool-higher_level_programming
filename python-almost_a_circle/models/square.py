#!/usr/bin/python3
'''square'''


from .rectangle import Rectangle


class Square(Rectangle):
    """
    Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''str'''
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''update'''
        attributes = ['id', 'size', 'x', 'y']
        if args:
            for attribute, value in zip(attributes, args):
                setattr(self, attribute, value)
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        '''dictionary'''
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
