# *********
# dir()
# *********
# dir() is built-in function, which returns list of the attributes and methods of any object,
# e.g. functions , modules, strings, lists, dictionaries etc.

# Syntax:
# dir({object})

# Return:
# dir() tries to return a valid list of attributes of the object it is called upon.
# it behaves differently with different type of objects:
# - For Class Objects, it returns a list of names of all the valid attributes and base attributes as well.
# - For Modules/Library objects, it tries to return a list of names of all the attributes, contained in that module.
# - If no parameters are passed it returns a list of names in the current local scope.

dir()
import random

# now random is added into current local scope
dir()

animals = ["cat", "dog", "fox"]
# will show all attributes for list
dir(animals)


# for user-defined objects __dir__ method may be redefined:
class Supermarket:

    # Function __dir()___ which list all
    # the base attributes to be used.
    def __dir__(self):
        return ['customer_name', 'product',
                'quantity', 'price', 'date']


my_cart = Supermarket()
# will result in __dir__ method return
dir(my_cart)


# *********
# __dict__
# *********
# Each custom class instance has magic attribute __dict__.
# It is a dictionary, which stores attributes, assigned to class instance.

class RegularClass:
    pass


obj = RegularClass()
obj.__dict__
# {}
obj.foo = 5
obj.__dict__
# {'foo': 5}
