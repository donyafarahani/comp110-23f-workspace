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

    #def scale_by(self, factor: int) -> None:
       # """Method that updates the x and y values."""
        #self.x *= factor
        #self.y *= factor

    #def scale(self, factor: int) -> Point:
       # """Method that creates a new point."""
       # return Point(self.x * factor, self.y * factor)
    
    def __str__(self) -> str:

        return f"x: {self.x}; y: {self.y}"
    

    def __mul__(self, factor) -> str:
        """Multiplycation operator overload."""
        new_x: self.x * factor
        new_y: self.y * factor
        return f"x: {new_x}; y: {new_y}"
    

    def __add__(self, add_val) -> str:
        """Addition operator overload."""
        new_x: self.x + add_val
        new_y: self.y * add_val
        return f"x: {new_x}; y: {new_y}"