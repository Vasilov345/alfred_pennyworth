from functools import wraps


def logged(func):
    # wraps function in being used to preserve decorated func metadata
    @wraps(func)
    def with_logging(*args, **kwargs):
        print("{} was called".format(func.__name__))
        return func(*args, **kwargs)

    return with_logging


@logged
def f(x):
    """does some math"""
    return x + x * x


print(f.__name__)  # prints 'f'
print(f.__doc__)  # prints 'does some math'
print(f(5))
