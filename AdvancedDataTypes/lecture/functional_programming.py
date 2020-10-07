import functools

# ***************************
# Functional-style programs
# ***************************
# Functional programming decomposes a problem into a set of functions.
# Ideally, functions only take inputs and produce outputs,
# and don’t have any internal state that affects the output produced for a given input.

# https://docs.python.org/3/howto/functional.html


# ******************
# anonymous function
# ******************
# 1. What is anonymous function
# In Python, anonymous function is a function that is defined without a name.
# While normal functions are defined using the def keyword, anonymous functions are defined using the lambda keyword.
# lambda-function is used for creating small, one-time use anonymous objects in Python

# 2. lambda - use-cases and syntax
# generally used as an argument to a higher-order function (a function that takes in other functions as arguments).
# e.g., with built-in functions like filter(), map() etc.

# lambda-operator may have arbitrary number of arguments, but only one expression.
# lambda arguments : expression
add = lambda x, y: x + y
# 2 and 3 will be passed to lambda function, their sum will be returned
print(add(2, 3))

# 3. lambda vs classic function
# Lambda
double = lambda x: x * 2
# number will be passed to lambda function and multiplied by 2
print(double(5))


# Equivalent classic function
def double(x):
    return x * 2


# number will be passed to double function and multiplied by 2
# result will be the same as above
print(double(5))

# ************************************
# Functional programming built-in funcs
# ************************************

# 1. sorted
# collects all the elements of the iterable into a list, sorts the list, and returns the sorted result.
rand_list = [5, 7, 1, 3]
# expression will return sorted list (from smaller to bigger)
print(sorted(rand_list))
# expression will return sorted list in a reversed order
print(sorted(rand_list, reverse=True))
# Out[289]: [7, 5, 3, 1]


# 2. map
# The map() function in Python takes in a function and a list. The function is applied for each element
# and resulting list is returned.

# Program to double each item in a list using map()
lst = [1, 5, 4, 6, 8, 11, 3, 12]
# lambda function is applied for every lst value.
lst_doubled = list(map(lambda x: x * 2, lst))

# 3. reduce
# Python’s reduce() implements a mathematical technique commonly known as folding or reduction.
# You’re doing a fold or reduction when you reduce a list of items to a single cumulative value.
# Python’s reduce() operates on any iterable—not just lists—and performs the following steps:
# Apply a function (or callable) to the first two items in an iterable and generate a partial result.
# Use that partial result, together with the third item in the iterable, to generate another partial result.
# Repeat the process until the iterable is exhausted and then return a single cumulative value.

# sum alternative
numbers = [0, 1, 2, 3, 4]


def my_add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result


functools.reduce(my_add, numbers)
# 0 + 1 = 1
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# Out[283]: 10

# get value from dict hierarchically
conf_dict = {"a": {"b": {"c": 3, "l": 4}, "f": 5}}
cls_sections = "a.b.c"
# get value from the dict based on keys in depth
print(functools.reduce(lambda d, k: d[k], cls_sections.split("."), conf_dict))

# 4. filter
# The filter() function in Python takes in a function (usually resulting in True or False) and a list as arguments.
# filter() is called with all the items in the list and a new list is returned:
# it contains only items for which the function evaluates to True.
# Program to filter out only the even items from a list
lst = [1, 5, 4, 6, 8, 11, 3, 12]
# lambda function will give True only if the value is even
lst_filter_even = list(filter(lambda x: (x % 2 == 0), lst))
