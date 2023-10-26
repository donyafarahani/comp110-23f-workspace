"""Combining two lists into a dictionary."""

__author__: str = "730661618"


def zip(L1: list[str], L2: list[int]) -> dict[str, int]:
    """The zip function checks if the 1st and 2nd lists are the same length and returns a dict with L1 as keys and L2 as values."""
    i: int = 0
    my_dict: dict[str, int] = {}
    if len(L1) != len(L2):
        return my_dict
    for k in L1:
        my_dict[k] = L2[i]
        i += 1
    
    return my_dict
    

print(zip(["Happy", "Tuesday"], [1, 2]))