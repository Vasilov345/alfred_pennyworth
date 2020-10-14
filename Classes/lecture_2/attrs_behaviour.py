# **********************
# property/setter/getter
# **********************
# 1. @property decorator can be used to make the method to be attribute-like accessible.
# 2. @property decorator can be used to create getters & setters in pythonic way.
#    Any kind of logic can be applied in getter or setter functions.

class Person:
    def __init__(self):
        self._age = 0

    # property decorator
    @property
    def age(self):
        print("getter method called")
        return self._age

    # a setter function
    @age.setter
    def age(self, a):
        if a < 18:
            raise ValueError("Sorry you age is below eligibility criteria")
        print("setter method called")
        self._age = a


mark = Person()
mark.age = 19
print(mark.age)  # method called, but looks like a regular attribute.


# ***************
# setattr/getattr
# ***************
# The setattr() function sets the value of the attribute of an object.
# Syntax: setattr(object, name, value)
# object - object whose attribute has to be set
# name - attribute name
# value - value given to the attribute

class Person:
    name = 'Adam'


p = Person()

# setting attribute name to John
setattr(p, 'name', 'John')
print('Name is:', p.name)

# setting an attribute not present in Person
setattr(p, 'age', 23)
print('Age is:', p.age)


# The getattr() method returns the value of the named attribute of an object.
# If not found, it returns the default value provided to the function.
# Syntax: getattr(object, name[, default]), which is equivalent to: object.name

class Person2:
    age = 23
    name = "Adam"


person = Person2()
print('The age is:', getattr(person, "age"))
print('The age is:', person.age)
