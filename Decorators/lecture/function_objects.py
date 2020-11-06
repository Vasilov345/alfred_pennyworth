# Functions return a value based on the given arguments
# Functions can be passed around, and used as arguments, just like any other value (e.g, string, int, float).

def foo(bar):
    return bar + 1


print(foo)
print(foo(2))
print(type(foo))


def call_foo_with_arg(foo_param, arg):
    return foo_param(arg)


print(call_foo_with_arg(foo, 3))


# * Task: Create 2 functions with arbitrary names and parameters,
# First — takes 1 argument and returns its exponent,
# Second takes 2 arguments — the above mentioned function and argument which is passed to that function.
# Second should return result of the first.


# ****************
# nested functions
# ****************

# Nested functions allow to define functions inside other functions.
# They can be used inside of parent function.

def parent():
    print("Printing from the parent() function.")

    def first_child():
        return "Printing from the first_child() function."

    def second_child():
        return "Printing from the second_child() function."

    print(first_child())
    print(second_child())


# second_child() - call to nested function outside f parent class will result in an error


# ******************************
# return function from function
# ******************************

def where_to_go(age):
    def kindergarten():
        return "should go to kindergarten"

    def school():
        return "should go to school"

    def university():
        return "it is never too late to go to university"

    if age < 6:
        return kindergarten
    elif 17 >= age >= 6:
        return school
    else:
        return university


anna = where_to_go(4)
andrii = where_to_go(12)
magdalyna = where_to_go(70)

print(anna())
print(magdalyna())
