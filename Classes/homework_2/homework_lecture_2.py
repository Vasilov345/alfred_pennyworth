import dataclasses

class Maths:
    add_num = lambda x, y: x + y


class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def margherita(cls):
        cls.ingredients = ['mozzarella', 'tomatoes']
        return cls

    @classmethod
    def prosciutto(cls):
        cls.ingredients = ['mozzarella', 'tomatoes', 'ham']
        return cls


class Concert:
    max_visitors_num = 0

    def __init__(self):
        self._visitors_count = 0

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, value):
        if value <= Concert.max_visitors_num:
            self._visitors_count = value
        else:
            self._visitors_count = self.max_visitors_num

@dataclasses.dataclass
class BookDataclass:

    title: str
    author: str
    pages_num: int


class Book:

    def __init__(self, title, author, pages_num):
        self.title = title
        self.author = author
        self.pages_num = pages_num

    def __str__(self):
        return str(BookDataclass(title=self.title, author=self.author, pages_num=self.pages_num))

