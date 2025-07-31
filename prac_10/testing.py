"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """
    Repeat string s, n times, with spaces in between.

    Args:
        s (str): The string to repeat
        n (int): Number of times to repeat the string

    Returns:
        str: The repeated string with spaces between each repetition
    """
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in.

    Args:
        word (str): The word to check
        length (int): The minimum length to compare against (default: 5)

    Returns:
        bool: True if word length is >= length, False otherwise

    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    # TODO 4: Fixed - Changed from > to >= to match test expectations
    return len(word) >= length


def sentence_format(phrase):
    """
    Format a phrase as a sentence, starting with a capital and ending with a single full stop.

    Args:
        phrase (str): The phrase to format

    Returns:
        str: The formatted sentence

    >>> sentence_format('hello')
    'Hello.'
    >>> sentence_format('It is an ex parrot.')
    'It is an ex parrot.'
    >>> sentence_format('python programming')
    'Python programming.'
    """
    # TODO 5: Created function to format phrases as sentences
    phrase = phrase.rstrip('.!?')
    return phrase.capitalize() + '.'


def run_tests():
    """Run the tests on the functions."""
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    car = Car(fuel=10)
    assert car.fuel == 10, "Car does not set fuel correctly when value is passed in"

    car_default = Car()
    assert car_default.fuel == 0, "Car does not set fuel correctly with default value"


run_tests()

# TODO 3: Enabled doctest execution
doctest.testmod()