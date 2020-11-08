# *********************************
# user-defined (custom) exceptions
# *********************************
# In Python, users can define custom exceptions by creating a new class.
# This exception class has to be derived, either directly or indirectly, from the built-in Exception class.
# Most of the built-in exceptions are also derived from this class.

# This is the standard way to define user-defined exceptions in Python:
# write common Error class for your program, and then derive from it.
class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass


# you need to guess this number
number = 10

# user guesses a number until he/she gets it right
while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!\n")
    except ValueTooLargeError:
        print("This value is too large, try again!\n")

print("Congratulations! You guessed it correctly.")


# *******************************
# customizing exception classes
# *******************************
# user-defined exception classes can be further customized to accept other arguments as per specific needs.
class SalaryNotInRangeError(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.salary} -> {self.message}"


salary = int(input("Enter salary amount: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)  # custom message may be passed


# also, SalaryNotInRangeError error may be caught within calling process:
def check_salary(salary):
    if not 5000 < salary < 15000:
        raise SalaryNotInRangeError(salary)


# calling process
try:
    check_salary(50)
except SalaryNotInRangeError as e:
    print(e.salary)
    print(e.message)
