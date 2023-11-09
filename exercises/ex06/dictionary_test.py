"""This is my dictionary test file for testing functions from ex06."""


__author__: str = "730611618"

from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


#Invert tests
def test_invert_empty_dict():
    """The function's given_dict arguement is an empty dictionary."""
    assert invert({}) == {}


def test_2keys_to_be_2values():
    """The given_func in the invert function will have 2 keys with 1 value each, which should return an inverted dictionary where the given keys are now the values."""
    assert invert({'Pepper': 'dog', 'Homer': 'cat'})


def test_5keys_to_be_5values():
    """The given_func in the invert function will have 4 keys with 1 value each, which should return an inverted dictionary where the given keys are now the values."""
    assert invert({'Horse': 'Barney', 'Cat': 'Snow', 'Dog': 'Wilson', 'Chicken': 'Noodle'}) == {'Barney': 'Horse', 'Snow': 'Cat', 'Wilson': 'Dog', 'Noodle' : 'Chicken'}


#Favorite color tests
def test_favorite_color_empty_dict():
    """The function's given_dict arguement is an empty dictionary."""
    assert favorite_color({}) == ''


def test_colors_with_same_count():
    """The given_dict has two colors with the same highest appearance, and the first color should be returned."""
    assert {'Carl': 'Purple', 'Bob': 'Red', 'Tod': 'Red', 'Shawn': 'Purple'} == 'Purple'


def test_colors_with_different_count():
    """The given_dict has two colors with the same highest appearance, and the first color should be returned."""
    assert {'Carl': 'Purple', 'Bob': 'Red', 'Tod': 'Orange', 'Shawn': 'Purple', 'Derrick': 'Orange', 'Delilah': 'Orange'} == 'Orange'


#Count tests
def test_count_empty_list():
    """The function's given_list arguement is an empty list."""
    assert count([]) == {}


def test_list_with_one_apearance_per_key():
    """The given_list containes distinct elements that each only appear once in the list."""
    assert count(['fish', 'dog', 'cat', 'wolf']) == {'fish': 1, 'dog': 1, 'cat': 1, 'wolf': 1}


def test_list_with_one_apearance_per_key():
    """The given_list containes elements, and their appearance counts are different."""
    assert count(['fish', 'fish', 'cat', 'fish', 'cat', 'dog', 'fish']) == {'fish': 4, 'cat': 2, 'dog': 1}


#Alphabetizer tests
def test_alphabetizer_empty_list():
    """The function's given_list arguement is an empty list."""
    assert alphabetizer([]) == {}


def test_list_of_all_lowercased_words():
    """The function's given_list has all lowercased words that need to be sorted into lists based on the first letter."""
    assert alphabetizer(['car', 'boy', 'cash', 'crack', 'box']) == {'c': ['car', 'cash', 'crack'], 'b': ['boy', 'box']}


def test_list_of_lower_and_uppercased_words():
    """The function's given_list has lower and uppercased words that need to be sorted into lists based on the first letter."""
    assert alphabetizer(['Car', 'boy', 'cash', 'Crack', 'Box', 'dog', 'duck', 'Big']) == {'c': ['Car', 'cash', 'Crack'], 'b': ['boy', 'Box', 'Big'], 'd': ['dog', 'duck']}


#Attendance log tests
def test_attendance_log_empty_arguements():
    """The function's given_dict arguement is an empty dictionary."""
    assert invert({}, '', '') == {}


def test_weekday_not_in_log():
    """The function is given a weekday that is not already in the attendance log."""
    attendance_log: dict = {'Monday': ['Sam', 'Derrick'], 'Tuesday': ['Alex', 'Justin']}
    assert update_attendance(attendance_log, 'Wednesday', 'Claire') == {'Monday': ['Sam', 'Derrick'], 'Tuesday': ['Alex', 'Justin'], 'Wednesday': ['Claire']}


def test_weekday_not_in_log():
    """The function is given a weekday that is already in the attendance log."""
    attendance_log: dict = {'Monday': ['Sam', 'Derrick'], 'Tuesday': ['Alex', 'Justin'], 'Wednesday': ['Claire']}
    assert update_attendance(attendance_log, 'Tuesday', 'Max') == {'Monday': ['Sam', 'Derrick'], 'Tuesday': ['Alex', 'Justin', 'Max'], 'Wednesday': ['Claire']}