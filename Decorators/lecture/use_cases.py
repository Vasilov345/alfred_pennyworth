# 1. as a timer — to see how long it took to run the function
# 2. rate limiting

from time import sleep


def sleep_decorator(function):
    """
    Limits how fast the function is called.
    """

    def wrapper(*args, **kwargs):
        sleep(2)
        return function(*args, **kwargs)

    return wrapper


@sleep_decorator
def print_number(num_param):
    return num_param


print(print_number(222))
for num in range(1, 6):
    print(print_number(num))

# 3. One of the most used decorators in Python is the login_required() decorator, which ensures
# that the user is logged in/properly authenticated before s/he can access a specific route (/secret, in this case)

"""
from functools import wraps
from flask import g, request, redirect, url_for


def login_required(f):
    @wraps(f)  # This preserves metadata of the wrapped function f
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)

    return decorated_function


@app.route('/secret')
@login_required
def secret():
    pass
"""

# 4. augment functions with code that logs calls made to them
# 5. check the types of passed arguments during debugging
