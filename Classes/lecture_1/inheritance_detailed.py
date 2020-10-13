# In python 3, every class is inherited from the base class object.
class A(object):
    pass


# is the same as:

class B:
    pass


# *********************
# Level of inheritance
# *********************
# The level of inheritance is the length of path from the top base class to the bottom derived class.
# A base class for any derived class could also be derived from other classes.
# https://blog.miyozinc.com/core-tutorials/cpp/cpp-inheritance-types/
# In multilevel inheritance, we inherit the classes at multiple separate levels.

# We have three classes X, Y and Z, where X is the super class, Y is its sub(child) class and Z is the sub class of Y.
class X:
    # properties of class X
    pass


class Y(X):
    # class Y inheriting property of class X
    # more properties of class Y
    pass


class Z(Y):
    # class Z inheriting property of class Y
    # thus, class Z also inherits properties of class X
    # more properties of class Z
    pass


# *********************
# Multiple inheritance
# *********************
# When a class inherits the characteristics of more than one class.

class Human:
    def __init__(self):
        print('class Human')


class Horse:
    def __init__(self):
        print('class Horse')


class Centaur(Human, Horse):
    def __init__(self):
        print('class Centaur')
        super().__init__()


obj1 = Centaur()


# ***********************
# Method resolution order
# ***********************
# MRO is used primarily to obtain the order in which methods should be inherited in the presence of multiple inheritance
# Python 3 uses the C3 linearization algorithm for MRO.
# https://medium.com/@__hungrywolf/mro-in-python-3-e2bcd2bd6851

Centaur.mro()  # [__main__.Centaur, __main__.Human, __main__.Horse, object]


# *********************
# __super__
# *********************
# Allows to call methods of the superclass in subclass.
# The primary use case of this is to extend the functionality of the inherited method.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


# super() is used to call the __init__ of Rectangle class, allowing to use it in Square class without repeating code.
# https://realpython.com/python-super/


# *********************
# attribute types
# *********************
# 1. public - can be freely used inside or outside of a class definition.
# 2. protected - should not be used outside of class definition
# 3. private - inaccessible and invisible.
# It 's neither possible to read nor write to those attributes, except inside of the class definition itself.

class Robot:
    def __init__(self, name=None, build_year=2000):
        self.__name = name
        self.__build_year = build_year

    def say_hi(self):
        if self.__name:
            print("Hi, I am " + self.__name)
        else:
            print("Hi, I am a robot without a name")

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_build_year(self, by):
        self.__build_year = by

    def get_build_year(self):
        return self.__build_year

    def __repr__(self):
        return "Robot('" + self.__name + "', " + str(self.__build_year) + ")"

    def __str__(self):
        return "Name: " + self.__name + ", Build Year: " + str(self.__build_year)


x = Robot("Marvin", 1979)
y = Robot("Caliban", 1943)
for rob in [x, y]:
    rob.say_hi()
    if rob.get_name() == "Caliban":
        rob.set_build_year(1993)
    print("I was built in the year " + str(rob.get_build_year()) + "!")
