# magic methods or dunder methods (dunder here means “Double Underscores”)

# *********************
# Object life time
# *********************
# 1. __call__
# __call__ method enables to write classes where the instances behave like functions and can be called like a function.
# if this method is defined, x(arg1, arg2, ...) is a shorthand for x.__call__(arg1, arg2, ...).
class Example:
    def __init__(self):
        print("Instance Created")

    def __call__(self):  # may be called with parameters as well
        print("Instance is called via special method")


e = Example()
# __call__ method will be called
e()


# 2. __new__
# https://www.geeksforgeeks.org/__new__-in-python/
# Whenever a class is instantiated __new__ and __init__ methods are called.
# __new__ method will be called when an object is created and __init__ method will be called to initialize the object.
# In the base class object, the __new__ method is defined as a static method which requires to pass a parameter cls.
# cls represents the class that is needed to be instantiated,
# and the compiler automatically provides this parameter at the time of instantiation.
class MyClass:
    def __new__(cls, *args, **kwargs):
        # statements
        return super(MyClass, cls).__new__(cls, *args, **kwargs)


# Note: Instance can be created inside __new__ method either by using super function
# or by directly calling __new__ method over object.
# That is instance = super(MyClass, cls).__new__(cls, *args, **kwargs) or
# instance = object.__new__(cls, *args, **kwargs)


# 3. __init__
# The __init__ method is run as soon as an object of a class is instantiated (i.e. created).
# The method is useful to do any initialization (i.e. passing initial values to object) needed to be done with object.

class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)


# __init__ method will be called
p = Person('Adolf')
p.say_hi()

# # The previous 2 lines can also be written as
Person('Swaroop').say_hi()


# 4. __del__
# __del__ is a destructor method which is called as soon as all references of the object are deleted
# i.e when an object is garbage collected
class Example:

    def __init__(self):
        print("Example Instance.")

    def __del__(self):
        print("Destructor called, Example deleted.")


obj = Example()
del obj


# More examples:
class Robot():

    def __init__(self, name):
        print(name + " has been created!")

    def __del__(self):
        print("Robot has been destroyed")


x = Robot("Tik-Tok")
y = Robot("Jenkins")
z = x
print("Deleting x")
del x  # destructor will not be called since z still references to the object
print("Deleting z")
del z
del y


# **********************
# Object representation
# **********************
# 1. __str__
# This method returns the string representation of the object.
# This method is called when print() or str() function is invoked on an object.
# If __str__ method is not implemented for class, built-in object implementation is used - actually calls __repr__ function.

# 2. __repr__
# Python __repr__() function returns the object representation. It could be any valid python expression such as tuple, dictionary, string etc.
#
# This method is called when repr() function is invoked on the object,
# in that case, __repr__() function must return a String otherwise error will be thrown.

# 3. __str__ vs __repr__:
# __str__ must return string object whereas __repr__ can return any python expression.
# If __str__ implementation missing then __repr__ is used as fallback. No fallback if __repr__ implementation missing.
# If __repr__ is returning String representation of the object, implementation of __str__ can be skipped.
# https://stackoverflow.com/questions/1436703/difference-between-str-and-repr

# A user defined class should also have a __repr__ if we need detailed information for debugging.
# And if we think it would be useful to have a string version for users, we create a __str__ function.
class Complex:

    # Constructor
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # For call to repr(). Prints object's information
    def __repr__(self):
        return 'Rational(%s, %s)' % (self.real, self.imag)

    # For call to str(). Prints readable form
    def __str__(self):
        return '%s + i%s' % (self.real, self.imag)


# Driver program to test above
t = Complex(10, 20)

str(t)  # same as print(t)
repr(t)  # same as simply t

# *********************
# Objects comparison
# *********************
# 1. __lt__ - implements the < operator.
# 2. __le__ - implements the <= operator.
# 3. __eq__ - implements the == operator.
# 4. __ne__ - implements the != operator.
# 5. __gt__ - implements the > operator
# 6. __ge__ - implements the >= operator

import math


class Vec2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vec2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __ne__(self, other):
        return not self.__eq__(other)


u = Vec2D(0, 1)
v = Vec2D(2, 3)
w = Vec2D(-1, 1)

a = u + v  # __add__ method will be triggered
a == w  # __eq__ method will be triggered

a = u - v  # __sub__ method will be triggered
a = u * v  # __mul__ method will be triggered

abs(u)  # __abs__ method will be triggered
u == v  # __eq__ method will be triggered
u != v  # __ne__ method will be triggered
