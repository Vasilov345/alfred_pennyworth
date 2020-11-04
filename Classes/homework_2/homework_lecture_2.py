import dataclasses
from typing import Any

"""
    Make class with one method "add_num" with 2 parameters, which returns sum of these parameters.
    Note: this method should not take instance as first parameter.
    """
class _num():

    def __init__(self):
            self._num = a + b

        # @property decorator can be used to create getters & setters in pythonic way.

    @property
    def _add_num(self):
        return self._add_num

    @add_num.setter
    def add_num(self, value):
        _add = _num()
        _add.add_num = a + b
        self._add_num(self): -> Any

print(_add.add_num)


from abc import ABC

class AbstractBase ('pizza1', 'pizza2'):
    __slots__ = 'pizza1', 'pizza2'

    """
    Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
    It should have 2 methods:
    margherita (['mozzarella', 'tomatoes']) and prosciutto (['mozzarella', 'tomatoes', 'ham'])
    which should create Pizza instances with predefined list of ingredients.
    Example:
        pizza1 = Pizza(["tomato", "cucumber"])
        pizza1.ingredients will equal to ["tomato", "cucumber"]
        pizza2 = Pizza.prosciutto()
        pizza2.ingredients will equal to ['mozzarella', 'tomatoes', 'ham']
    """

    def __init__(self, pizza1, pizza2) -> Any:
        self.pizza1 = pizza1 ["tomato", "cucumber"]
        self.pizza2 = pizza2 ["tomato", "cucumber"]
        self.pizza2 = Pizza.prosciutto()
        self.pizza2.ingredients = ['mozzarella', 'tomatoes', 'ham']

#pizza1 = Pizza (["tomato", "cucumber"])
#pizza1.ingredients = ["tomato", "cucumber"]
#pizza2 = Pizza.prosciutto()
#pizza2.ingredients = ['mozzarella', 'tomatoes', 'ham']

def __repr__(type):
    return f'{type(self).__init__}({repr(self.pizza1)}, {repr(self.pizza2)})'


# """
# Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
# In case of setting visitors_count - max_visitors_num should be checked,
# if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
# Example:
#     Concert.max_visitor_num = 50
#     concert = Concert()
#     concert.visitors_count = 1000
#     print(concert.visitors_count)  # 50
# """

class Concert:
    def __init__(self):
        self.Concert.max_visitor_num = 50

        # @property decorator can be used to create getters & setters in pythonic way.

    @property
    def concert(self):
        return self.concert.visitors_count

concert = Concert()
concert.visitors_count = 1000

print(concert.visitors_count)


from dataclasses import dataclass

@dataclasses.dataclass(frozen=True)
class BookDataclass:
    """
            Create dataclass with 3 fields - title (str), author (str), pages_num (int)
            """
    # Attributes Declaration
    # using Type Hints - Class with attributes
    title: str
    author: str
    pages_num: int = 0

book = Book(title="str", author="str", pages_num ="int = 0")
print(book[1])


@BookDataclass
class RegularBook:
    """
           Create regular class taking 3 params on init - title, author, pages_num
           Make its str() representation the same as for BookDataclass defined above.
           """
    title: str
    author: str
    pages_num: int = 0

    def __init__(self, title, author, pages_num):
        self.title = title
        self.author = author
        self.pages_num = pages_num

print(RegularBook)


    # HW#5 homework_lecture_2.py
