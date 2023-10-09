"""This is my ex04 for lists."""
author: str = "730661618"


def all(num_list: list[int], num: int) -> bool:
    """This function finds if all the elements of a list are the same value as an integer."""
    value: int = 0
    i: int = 0

    if len(num_list) == 0:
        return False
    
    while i < len(num_list):
        if num_list[i] == num:
            value += 1
        else: 
            return False
        i += 1

        if value == len(num_list):
            return True


def max(num_list: list[int]) -> int:
    """This function finds the maximum value in a given list."""
    if len(num_list) == 0:
        raise ValueError("max() arg is an empty List")
    
    i: int = 0
    max: int = num_list[0]

    while i <= (len(num_list) - 1):
        if num_list[i] > max:
            max = num_list[i]
        i += 1
    return max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """This function tests if list1 and list2 are equal with the same elements in the same order."""
    if list1 == list2:
        return True
    else:
        return False