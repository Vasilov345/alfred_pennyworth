# ******************************
# Exceptions in Python
# ******************************
# Python has many built-in exceptions that are raised when program encounters error (smth in the program goes wrong).
# https://docs.python.org/3.8/library/exceptions.html
# When these exceptions occur, the Python interpreter stops the current process and passes it to the calling process
# until it is handled. If not handled, the program will crash.
# In Python, an error can be a syntax error or an exception.
# Syntax errors occur when the parser detects an incorrect statement.
# Exception error occurs when syntactically correct Python code results in an error.


# **********************
# try - except block
# **********************
# The try and except block in Python is used to catch and handle exceptions.
# Python executes code following the try statement as a “normal” part of the program.
# The code that follows the except statement is the program’s response to any exceptions in the preceding try clause.
# If no exception occurs, the except block is skipped and normal flow continues(for last value).
# But if any exception occurs, it is caught by the except block (first and second values).

# Here 'a' causes ValueError and 0 causes ZeroDivisionError.
import sys

random_list = ['a', 0, 2]

for entry in random_list:
    try:
        print("The entry is", entry, "\n")
        r = 1 / int(entry)
    except:
        print("Oops!", sys.exc_info()[0], "occurred.\n")

# Since every exception in Python inherits from the base Exception class,
# the above task can be performed in the following way:

for entry in random_list:
    try:
        print("The entry is", entry, "\n")
        r = 1 / int(entry)
    except Exception as e:
        print("Oops!", e.__class__, "occurred.\n")

# It is possible to specify which exceptions an except clause should catch.
for entry in random_list:
    try:
        print("The entry is", entry, "\n")
        r = 1 / int(entry)
    except ValueError:
        print(f"value {entry} can not be converted to int")
    except ZeroDivisionError:
        print(f"could not divide by zero")
    except Exception as e:
        print("Some unexpected exceprion happened")

# ************
# else
# ************
# In some situations, there is a need to run a certain block of code if the code inside try ran without any errors.
# For these cases, optional else keyword may be used with the try statement.

# program to print the reciprocal of even numbers
try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except Exception:
    print("Not an even number!")
else:
    reciprocal = 1 / num
    print(reciprocal)

# Note: However, 0 is passed, we get ZeroDivisionError as the code block inside else is not handled by preceding except

# ************
# finally
# ************
# The try statement in Python can have an optional finally clause.
# This clause is executed no matter what, and is generally used to release external resources.
try:
    with open("test.txt", encoding='utf-8') as f:
        ...
        # perform file operations
except FileNotFoundError:
    pass
finally:
    print("Finished working with file")


# ***********
# raise
# ***********
# If you want to throw an error when a certain condition occurs, it is possible to use raise keyword:

def check_value(x):
    if x > 5:
        raise Exception('x should not exceed 5. The value of x was: {}'.format(x))


try:
    check_value(10)
except Exception as e:
    print(e)

