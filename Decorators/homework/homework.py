# 1. double_result
# This decorator function should return the result of another function multiplied by two
def double_result(func):
    # return function result multiplied by two
    pass


def add(a, b):
    return a + b


add(5, 5)  # 10


@double_result
def add(a, b):
    return a + b


add(5, 5)  # 20


# 2. only_even_parameters
# This decorator function should only allow a function to have even parameters,
# otherwise return the string "Please only use even numbers!"

def only_even_parameters(func):
    # if args passed to func are not even - return "Please only use even numbers!"
    pass


@only_even_parameters
def add(a, b):
    return a + b


add(5, 5)  # "Please add even numbers!"
add(4, 4)  # 8


@only_even_parameters
def multiply(a, b, c, d, e):
    return a * b * c * d * e


# 3. logged
# Write a decorator which wraps functions to log function arguments and the return value on each call.
# Provide support for both positional and named arguments (your wrapper function should take both *args
# and **kwargs and print them both):

def logged(func):
    # log function arguments and its return value
    pass


@logged
def func(*args):
    return 3 + len(args)


func(4, 4, 4)


# you called func(4, 4, 4)
# it returned 6


# 4. type_check (see pass_args_to_decorator.py from lecture for example)
# you should be able to pass 1 argument to decorator - type.
# decorator should check if the input to the function is correct based on type.
# If it is wrong, it should print("Bad Type"), otherwise function should be executed.

def type_check(correct_type):
    # put code here
    pass


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
times2('Not A Number')  # "Bad Type" should be printed, since non-int passed to decorated function


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])  # "Bad Type" should be printed, since non-str passed to decorated function
