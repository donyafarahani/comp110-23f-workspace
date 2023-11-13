"""Challenge question 07."""

from __future__ import annotations


class Point:
    """My class named Point that has attributes of x and y floats."""
    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """This is my constructor."""
        self.x = x_init
        self.y = y_init

    def __str__(self) -> str:
        """This method returns the values of self.x and self.y as a string to be later nicely printed."""
        return f"x: {self.x}; y: {self.y}"
    
    def __mul__(self, factor: int | float) -> Point:
        """Multiplycation operator overload."""
        self.x *= factor
        self.y *= factor
        return Point(self.x, self.y)
    
    def __add__(self, add_val: int | float) -> Point:
        """Addition operator overload."""
        self.x += add_val
        self.y += add_val
        return Point(self.x, self.y)