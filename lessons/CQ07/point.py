"""Challenge question 07."""

from __future__ import annotations


class Point():
    """My class named Point that has attributes of x and y floats."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """This is my constructor."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Method that updates the x and y values."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Method that creates a new point."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point