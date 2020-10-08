id(object)
# 1. What does id function stand for:
# Return the “identity” of an object.
# This is an integer which is guaranteed to be unique and constant for this object during its lifetime.
# Two objects with non-overlapping lifetimes may have the same id() value.
# CPython implementation detail: This is the address of the object in memory.
lst = [1, "3", [2, 3]]
# show identity of first, second and third lst element
print(id(lst[0]))
print(id(lst[1]))
print(id(lst[2]))

# 2. objects cache - instrument for memory optimization:
# The current implementation keeps an array of integer objects for all integers between -5 and 256,
# when you create an int in that range you actually just get back a reference to the existing object.
a = 257
b = 257

print(id(a))
# identity of b differs from a (if Python code was not precompiled)
print(id(b))

a = 256
b = 256

print(id(a))
# identity of b is the same as a
print(id(b))
