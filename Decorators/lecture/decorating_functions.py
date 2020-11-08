# "decoration" is just a way to run extra processing steps before and after function execution with "explicit" syntax.
# Put simply, decorators wrap a function, modifying its behavior.

# It comes in two flavors:
# 1. Function decorators specify special operation modes for both simple functions and classes’ methods
#    by wrapping them in an extra layer of logic implemented as another function, usually called a metafunction
# 2. Class decorators do the same for classes, adding support for management of whole objects and their interfaces

def my_decorator(some_function):
    def wrapper():
        print("Something is happening before some_function() is called.")
        some_function()
        print("Something is happening after some_function() is called.")

    return wrapper


def just_some_function():
    print("Wheee!")


just_some_function = my_decorator(just_some_function)
just_some_function()




