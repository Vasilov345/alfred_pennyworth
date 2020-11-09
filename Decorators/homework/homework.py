# 1. double_result
# This decorator function should return the result of another function multiplied by two
def double_result(func):
    def inner(*args, **kwargs):
        return func(*args, **kwargs) * 2

    return inner


def add(a, b):
    return a + b


add(5, 5)  # 10


@double_result
def add(a, b):
    return a + b


add(5, 5)  # 20


#2. only_even_parameters
# This decorator function should only allow a function to have even parameters,
# otherwise return the string "Please only use even numbers!"

def only_even_parameters(func):
    def inner(*args, **kwargs):
        for i in args:
            if i % 2 != 0:
                print("Please only use even numbers!")
                break

        return func(*args, **kwargs)

    return inner


@only_even_parameters
def add(a, b):
    return a + b


add(5, 5)  # "Please add even numbers!"
print(add(4, 4))  # 8


@only_even_parameters
def multiply(a, b, c, d, e):
    return a * b * c * d * e


# import module logging
import logging

# create logger with name main directory
logger = logging.getLogger(__name__)
logger_1 = logging.getLogger(__name__)
# set Level to logging
logger.setLevel(logging.DEBUG)
logger_1.setLevel(logging.DEBUG)
# create handler fo "*args" to input onto console window
arg_handler = logging.StreamHandler()
kwarg_handler = logging.StreamHandler()
# set level to handler
arg_handler.setLevel(logging.DEBUG)
kwarg_handler.setLevel(logging.DEBUG)
# create a formatter to arg_handler
arg_kwarg_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# add formatter to arg handler
arg_handler.setFormatter(arg_kwarg_formatter)
kwarg_handler.setFormatter(arg_kwarg_formatter)
logger.addHandler(arg_handler)
logger_1.addHandler(kwarg_handler)


# 3. logged
# Write a decorator which wraps functions to log function arguments and the return value on each call.
# Provide support for both positional and named arguments (your wrapper function should take both *args
# and **kwargs and print them both):

def logged(func):
    def inner(*args, **kwargs):
        if (args):
            logger.debug(f'The function \'*args\' arguments are {args}')
            doing_func = func(*args, **kwargs)
            logger.error(f'The return value of the function -  {doing_func}')
            return doing_func

        else:
            logger_1.debug(f'The function \'*kwargs\' arguments are {kwargs}')
            doing_func = func(*args, **kwargs)
            logger_1.error(f'The return value of the function -  {doing_func}')
            return doing_func

    return inner


# log function arguments and its return value


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


@logged
def func_1(**kwargs):
    l = [ kwargs[ i ] for i in kwargs ]
    return sum(l)


print(func_1(g=777, t=789))


# you called func(4, 4, 4)
# it returned 6


# 4. type_check (see pass_args_to_decorator.py from lecture for example)
# you should be able to pass 1 argument to decorator - type.
# decorator should check if the input to the function is correct based on type.
# If it is wrong, it should print("Bad Type"), otherwise function should be executed.

def type_check(correct_type):
    def outer(func):
        def inner(*args, **kwargs):
            if correct_type == type(*args):
                if correct_type == int:
                    res = func(*args, **kwargs)
                    return res
                elif correct_type == str:
                    print(type(*args))
                    for i in args:
                        g = i.split()
                        return (g[ 0 ])
            else:
                print('Bad Type')

        return inner

    return outer


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
times2('Not A Number')  # "Bad Type" should be printed, since non-int passed to decorated function


@type_check(str)
def first_letter(word):
    return word[ 0 ]


print(first_letter('Hello World'))
first_letter([ 'Not', 'A', 'String' ])  # "Bad Type" should be printed, since non-str passed to decorated function
