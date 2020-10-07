from typing import List, Dict

Alphabet = List[Dict[str, int]]


def generate_alphabet() -> Alphabet:
    """
    Generate list of dicts.
    Where each dict contain 1 pair of key/value
    key - letter from alphabet
    value - random int value from 0 to 100

    Examples:
        generate_alphabet()
    >>>
    [
        {'a': 5}, {'b': 57}, {'c': 23}, {'d': 57}, {'e': 88}, {'f': 86}, {'g': 12}, {'h': 41}, {'i': 8}, {'j': 50},
        {'k': 1}, {'l': 61}, {'m': 79}, {'n': 69}, {'o': 3}, {'p': 30}, {'q': 75}, {'r': 70}, {'s': 9},
        {'t': 57}, {'u': 34}, {'v': 70}, {'w': 13}, {'x': 86}, {'y': 12}, {'z': 82}
    ]
    """
    pass


def sort_alphabet(data: Alphabet) -> Alphabet:
    """
    Sort incoming alphabet by int values.
    Examples:
        sort_alphabet([{'a': 5}, {'b': 57}, {'c': 23}])
        >>> [{'a': 5}, {'c': 23}, {'b': 57}]
    """
    pass
