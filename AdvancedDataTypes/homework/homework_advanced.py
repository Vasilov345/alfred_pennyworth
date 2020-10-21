from typing import List, Dict
import random
import string
import operator

Alphabet = List[Dict[str, int]]


def generate_alphabet() -> Alphabet:
    # Alphabet =[]
    # for latter in string.ascii_lowercase:
    #   Alphabet.append(dict([(latter, random.randint(0, 100))]))
    # return Alphabet

    return ([dict([(words, random.randint(0, 100))]) for words in string.ascii_lowercase])


def sort_alphabet(data: Alphabet) -> Alphabet:
    Alphabet_sort = []
    list_1 = []
    for i in data:
        list_1 += i.items()
    list_1.sort(key=lambda x: x[1])
    for i in list_1:
        Alphabet_sort.append(dict([(i[0], i[1])]))
    return Alphabet_sort