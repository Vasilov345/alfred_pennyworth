# ***********************
# Dataclass vs NamedTuple
# ***********************
# Data Class is a type of class that is used to store data without any functionality.
# These data classes are just regular classes having the main purpose to store state and data
# without knowing the constraints and logic behind it.
# Also it is easy to validate attribute values types.
import dataclasses


@dataclasses.dataclass
# Class with attributes
class Article:
    """A class for holding an article content"""

    # Attributes Declaration
    # using Type Hints
    topic: str
    contributor: str
    language: str
    upvotes: int


# A DataClass object
article = Article("DataClasses", "nightfury1", "Python", 1)
print(article)
print(article.upvotes)
# dataclass instance can be mutated
article.new_attr = 5
print(article.new_attr)

# The NamedTuple is a class that contains the data like a dictionary format stored under the ‘collections‘ module.
# It stores the data in a key-value format where each key is mapped to values.
# Data is accessed using a specific key or can use the indexes.

# Python script to demonstrate namedtuple()

import collections

# Declaring namedtuple()
Contributor = collections.namedtuple('Contributor', ['topic', 'author', 'post'])

# Adding values
c = Contributor('Difference between DataClass vs NamedTuple in Python',
                'night_fury1',
                'Technical Content Writer Intern')

c2 = Contributor(topic="some topic", post="post", author="author")
print(c2[1])  # even if arguments are passed by key in random order, indexation will refer to declaration

# Access using index
print("The Article Topic : ", end="")
print(c[0])

# Access using name
print("The Article Contributor Name : ", end="")
print(c.author)

# Access using getattr()
print("The Article Contributor Post : ", end="")
print(getattr(c, 'post'))


# ***********************
# Frozen dataclass
# ***********************
# Frozen dataclass looks very similar to regular dataclass, but it is immutable.
@dataclasses.dataclass(frozen=True)
class Book:
    title: str
    author: str


book = Book(title="Fahrenheit 451", author="Bradbury")
# frozen dataclass instance can not be mutated - dataclasses.FrozenInstanceError is raised
# book.pages_num = 400


# To read: https://habr.com/ru/post/415829/
