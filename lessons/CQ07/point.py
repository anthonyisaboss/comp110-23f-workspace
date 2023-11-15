"""Point class work."""

from __future__ import annotations


class Point:
    """Rahhhhhhhhhh."""
    x: float
    y: float

    def __init__(self, x_init: float = 0, y_init: float = 0):
        """Constructing it."""
        self.x = x_init
        self.y = y_init
    
    def scale_by(self, factor: int) -> None:
        """Going to be scaling the x and y."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """Going to be creating the class."""
        new: Point = Point(self.x * factor, self.y * factor)
        return new
    
    def __str__(self) -> str:
        """Going to return a string."""
        string1: str = f"x: {self.x}; y: {self.y}"
        return string1
    
    def __mul__(self, factor: int | float) -> Point:
        """Leet code u suck."""
        new: Point = Point()
        new.x = self.x * factor
        new.y = self.y * factor
        return new
    
    def __add__(self, addition: int | float) -> Point:
        """Addibg together."""
        new: Point = Point()
        new.x = self.x + addition
        new.y = self.y + addition
        return new