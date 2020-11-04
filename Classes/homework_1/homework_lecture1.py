class CustomInt(int):
    """
    Make class for custom int, which will behave "vice versa" for comparison operations:
    e.g., int < int means less then, but custom int < int should equal custom int > int.
    Take into account <, >, >=, <=
    ** try to achieve this without __init__ rewriting
    """

    def __init__(self, x):
        self.x = x

    def __gt__(self, other):
        return self.x < other.x

    def __lt__(self, other):
        return self.x > self.x

    def __le__(self, other):
        return self.x >= other.x

    def __ge__(self, other):
        return self.x <= other.x


class PersonWithLimitedSkills:
    """
    Make class which is limited to 2 actions - eat and sleep
    Any other attributes addition should result in an error.
    """
    __isfrozen = False

    def __setattr__(self, key, value):
        if self.__isfrozen and not hasattr(self, key):
            raise TypeError("%r is a frozen class" % self)
        object.__setattr__(self, key, value)

    def _freeze(self):
        self.__isfrozen = True

    def eat(self):
        print('This men now is eating!')

    def sleep(self):
        print("I'm sleeping don't disturb me!")


class HiddenAttrs:
    """
    Make class which never tells about its attributes.
    Its attribute list is always empty and attributes dictionary is always empty.
    """
    def __dir__(self):
        return []

    def __dict__(self):
        return {}


class CallableInstances:
    """
        Make class which takes func parameter on initialization, which is a callable that can be passed.
    Then object of this class may be called - callable passed on init will be called with passed parameters.
    """
    def __init__(self, f):
        self._f = f

    def __call__(self, *args, **kwargs):
        return self._f(*args, **kwargs)



