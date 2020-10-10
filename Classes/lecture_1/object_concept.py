# ******************
# Instance of class
# ******************
# A class is a blueprint for the object. It defines attributes and methods.
# - Attribute is a variable stored in an instance or class.
# - Method is a function stored in an instance or class.
# We can think of class as an sketch of a parrot with labels.
# It contains all the details about the name, colors, size etc.
# Based on these descriptions, we can study about the parrot. Here, parrot is an object.
#
# The example for class of parrot can be :
class Parrot:  # class keyword is used to define an empty class Parrot.
    pass


# From class, instances are constructed. An instance is a specific object created from a particular class.
# An object (instance) is an instantiation of a class.
# When class is defined, only the description for the object is defined. Therefore, no memory or storage is allocated.

kesha = Parrot()
id(Parrot)
# is different from Parrot
id(kesha)


class Parrot:
    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age


blu = Parrot("Blu", 10)  # instantiate Parrot class/ create obj of class
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))


# ******************
# Class object
# ******************

# 1. Classes are objects in that they are manipulable in Python code just like any object:
# can be passed around to functions, assigned with attributes etc.
class Foo:
    def __init__(self):
        print("created foo")

    def __call__(self, *args, **kwargs):
        pass


def describe(python_obj):
    print("Value: {}".format(python_obj))
    print("Address: {}".format(id(python_obj)))


random_objects = [Foo, Foo(), "foo"]
describe(random_objects[0])

foo = Foo()
foo()


# 2. like all objects, classes are instantiated at runtime, and can be modified further after creation.
# That is, a class definition is code that is executed rather than a structure that is compiled before anything runs:
# class can "bake in" things that are only known when the program is run, such as environment variables or user input.
# These are evaluated once when the class is declared and then become a part of the class.
# This is different from compiled languages like C# which require this sort of behavior to be implemented differently.

class Foo(object):
    pass


f = Foo()
f.a = "a"  # assigns attribute on instance f
Foo.b = "b"  # assigns attribute on class Foo, and thus on all instances including f

print(f.a, f.b)

# 3. classes, like any object, are built from classes.
# Just as an object is built from a class, so is a class built from a special kind of class called a metaclass.
# You can write your own metaclasses to change how classes are defined.

# ** Metaclasses:
# “Metaclasses are deeper magic than 99% of users should ever worry about.
# If you wonder whether you need them, you don’t
# (the people who actually need them know with certainty that they need them, and don’t need an explanation about why).”
# — Tim Peters
# https://realpython.com/python-metaclasses/


# ******************
# type of object
# ******************
# type() will only return the immediate type of the object, but won’t be able to tell about type inheritance.
class Test1:
    pass


class Test2(Test1):
    pass


obj = Test2()
# will give True
print(type(obj) is Test2)
# will give False
print(type(obj) is Test1)

# will give True
isinstance(obj, Test2)
# will give True
isinstance(obj, Test1)


# ******************
# type == class
# ******************
class Foo:
    pass


x = Foo()

type(x)
# <class '__main__.Foo'>

type(Foo)
# <class 'type'>

# The type of x is class Foo. But the type of Foo, the class itself, is type. In general, the type of any class is type.
# The type of the built-in classes is also type:
type(int)  # <class 'type'>

# For that matter, the type of type is type as well:
type(type)  # <class 'type'>

# type is a metaclass, of which classes are instances.
# Just as an ordinary object is an instance of a class, any new-style class in Python,
# and thus any class in Python 3, is an instance of the type metaclass.
#
# In the above case:
# - x is an instance of class Foo.
# - Foo is an instance of the type metaclass.
# - type is also an instance of the type metaclass, so it is an instance of itself.
