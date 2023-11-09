"""This is my ex06 assigment for comp 110."""

__author__: str = "730661618"


def invert(given_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the key and values of given_dict."""
    invert_dict: dict[str, str] = {}

    for key in given_dict:
        if given_dict[key] in invert_dict:
            raise KeyError("Two same keys can't be in one dictionary.")
        invert_dict[given_dict[key]] = key
    
    return invert_dict


def favorite_color(given_dict: dict[str, str]) -> str:
    """Function takes in given_dict of names and colors, and checks to see what color appears the most."""
    color_count: dict[str, int] = {}

    for key in given_dict:
        if given_dict[key] in color_count:
            color_count[given_dict[key]] += 1
        else: 
            color_count[given_dict[key]] = 1

    fav_color: str = ''
    highest_color_count: int = 0

    for key in color_count:
        if color_count[key] > highest_color_count:
            highest_color_count = color_count[key]
            fav_color = key
    
    return fav_color


def count(given_list: list[str]) -> dict[str, int]:
    """Each key is a unique value of given_list and each value for that key is the count of times the 'key' appears in given_list."""
    my_dict: dict[str, int] = {}
    for elem in given_list:
        if elem in my_dict:
            my_dict[elem] += 1
        else:
            my_dict[elem] = 1

    return my_dict


def alphabetizer(given_list: list[str]) -> dict[str, list[str]]:
    """Each key is a unique letter from alphabet and its value is a list of words, taken from given_list, that begin with that unique letter."""
    my_dict: dict[str, list[str]] = {}

    for word in given_list:
        lowercased = word.lower()
        if lowercased[0] in my_dict:
            my_dict[lowercased[0]].append(word)
        else:
            my_dict[lowercased[0]] = [word]

    return my_dict


def update_attendance(log: dict[str, list[str]], week_day: str, student: str) -> dict[str, list[str]]:
    """Function will update with log of days (key) and list of students (value) with the students that attend on specified days."""
    if week_day in log:
        if not (student in log[week_day]):
            log[week_day].append(student)
    else: 
        log[week_day] = [student]
    return log