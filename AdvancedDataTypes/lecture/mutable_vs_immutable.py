# 1. difference betw. mutable and immutable objects:
# The value of some objects can change.
# Mutable - objects whose value can change;
# Immutable - objects whose value is unchangeable once they are created.

# Mutable
#     list
#     dict
#     set
#     bytearray
#     user-defined classes (unless specifically made immutable)

# Immutable
#     int
#     float
#     decimal
#     complex
#     bool
#     string
#     tuple
#     range
#     frozenset
#     bytes

# 2. Mutable vs immutable examples (with id)
# Immutability examples:
a = (1, 2, 3)
# get the identity of a
print(id(a))
a += (4, 5)
# now identity of tuple is changed
print(id(a))

s = "abc"
# get the identity of s
print(id(s))
s += "de"
# id of str is changed
print(id(s))

i = 5
print(id(i))
i += 10
# id of int is changed
print(id(i))

# Mutability examples:
l = ["p", "j"]
# get the identity of l
print(id(l))
l += "y"
# id of list is not changed
print(id(l))

ss = {4, 5, 6}
# get the identity of ss
print(id(ss))
ss.add(7)
# id of set is not changed
id(ss)


# 3. passing mutable and immutable arguments to functions:
# All arguments are passed by object reference, but
# - immutable arguments passing acts like call-by-value, they can't be changed within the function
# - mutable arguments can be changed in place in the function.

# Mutable example:
def my_func(l):
    l.append(1)


my_list = [5, 6]
# my_list will be populated with 1 value
my_func(my_list)


# * Bonus info
def append_one(l=[]):
    l.append(1)
    return l


# after every function call l 1 will be added to l - [1, 1, 1]
append_one()
append_one()
append_one()


# Immutable example:
def my_func_immutable_arg(s):
    s += "ending"
    print(s)  # prints "crazy ending"


s = "crazy "
# s will left unchanged
my_func_immutable_arg(s)
