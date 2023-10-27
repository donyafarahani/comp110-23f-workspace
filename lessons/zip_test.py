"""Test my zip function."""

__author__: str = "730661618"

from lessons.zip import zip


def test_empty_lists():
    """Zip function arguements are empty lists, making an empty my_dict."""
    assert zip([], []) == {}


def test_3keys_3values():
    """Function tests if 3 keys in test_list1 correctly pair with the values in test_list2."""
    test_list1: list[str] = ['banana', 'apple', 'pie']
    test_list2: list[int] = [1, 2, 3]
    assert zip(test_list1, test_list2) == {'banana': 1, 'apple': 2, 'pie': 3}


def test_2keys_2values():
    """Function tests if 2 keys in test_list1 correctly pair with the values in test_list2."""
    test_list1: list[str] = ['people', 'driver']
    test_list2: list[int] = [1, 2]
    assert zip(test_list1, test_list2) == {'people': 1, 'driver': 2}