"""Intro to object orientated programming."""

from __future__ import annotations

_author_ = "730464992"


class Point:
    """Mutating a point."""
    def __init__(self, x: float = 0.0, y: float = 0.0):
        """Creating parameters."""
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """Sets values of the parameters."""
        return f'x: {self.x}; y: {self.y}'
    
    def __mul__(self, factor: int | float) -> Point: 
        """Creates a new point by multiplying x and y."""
        if type(factor) in (int, float):
            return Point(self.x * factor, self.y * factor)
        else:
            raise TypeError("Factor must be an int or float.")
    
    def __add__(self, factor: int | float) -> Point: 
        """Creates new point by adding to x and y."""
        if type(factor) in (int, float):
            return Point(self.x + factor, self.y + factor)
        else:
            raise TypeError("factor must return an int or float.")


my_point = Point(1.0, 2.0)
print(str(my_point))

new_point = my_point * 3.0
print(new_point)

my_point = my_point + 3.0
print(my_point)