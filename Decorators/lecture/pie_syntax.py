# A function decorator is placed above the def statement that defines a function or method.
# It consists of the @ symbol, followed by what we call a metafunction — a function (or other callable object)
# that manages another function.

# without pie syntax
def my_decorator(my_func):
    def wrapper():
        print("before my_func() is called.")
        my_func()
        print("after my_func() is called.")

    return wrapper


def some_function():
    print("Wheee!")


some_function = my_decorator(some_function)
some_function()


# with pie syntax
def my_decorator_pie(my_func):
    def wrapper():
        print("before my_func() is called")
        my_func()
        print("after my_func() is called")

    return wrapper


@my_decorator_pie
def some_function_pie():
    print("Wheee!")


some_function_pie()  # the same results as the above call
