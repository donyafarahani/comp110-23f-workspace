"""Suming the elements of a list using different loops."""
__author__: str = "730661618"


def w_sum(vals: list[float]) -> float:
    """This function uses a while loop to get the sum of a given list."""
    value: float = 0.0
    i: int = 0
    while i < len(vals):
        value += vals[i]
        i += 1
    return value


def f_sum(vals: list[float]) -> float:
    """This function uses a for loop to get the sum of a given list."""
    value: float = 0.0
    for x in vals:
        value += x
    return value


def f_range_sum(vals: list[float]) -> float:
    """This function uses a for loop and range to get the sum of a given list."""
    value: float = 0.0
    for i in range(0, len(vals)):
        value += vals[i]
    return value