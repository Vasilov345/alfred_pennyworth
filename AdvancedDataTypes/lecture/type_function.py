# type() returns class type of the argument(object) passed as parameter.
# type() function is mostly used for debugging purposes.
# With one argument, return the type of an object.
# The return value is a type object and generally the same object as returned by object.__class__.

# built-in types
l = {1, 2, 3}
# show class attribute
print(l.__class__)
# see object type, which is the same as l.__class__ (set)
print(type(l))


# custom types
class Dog:
    pass


napoleon = Dog()
# get the type of custom type - __main__.Dog
# ‘__main__.’ before the class name because it is local to the current module.
print(type(napoleon))
# checking instance of napoleon object wii give True
isinstance(napoleon, Dog)
