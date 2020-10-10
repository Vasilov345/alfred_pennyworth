# *********
# __add__
# *********
# The magic method for the "+" sign
# The mechanism works like this:
# If we have an expression "x + y" and x is an instance of class K, then Python will check the class definition of K.
# If K has a method __add__ it will be called with x.__add__(y), otherwise we will get an error message

class MyDict(dict):

    def __add__(self, other):
        self.update(other)
        return MyDict(self)


a = MyDict({'de': 'Germany'})
b = MyDict({'sk': 'Slovakia'})

# equivalent to a.__add__(b)
a + b


# *********
# __sub__
# *********
# The magic method for the "-" sign
class MyInt(int):
    def __sub__(self, val):
        return self.numerator - 100


a = MyInt(200)
a - 3  # will subsract 100 from a value


# *********
# __mul__
# *********
# The magic method for the "*" sign
class Multiplier:

    def __init__(self, num):
        self.num = num

    def __mul__(self, val):
        return self.num * val


obj = Multiplier(6)
obj * 10  # __mul__ method will be called


class FakeMultiplier:

    def __init__(self, num):
        self.num = num


obj2 = FakeMultiplier(10)
# Will give an error
obj2 * 100
