class CustomInt(int):
    """
    Make class for custom int, which will behave "vice versa" for comparison operations:
    e.g., int < int means less then, but custom int < int should equal custom int > int.
    Take into account <, >, >=, <=
    ** try to achieve this without __init__ rewriting

    x<y calls x.__lt__(y), x<=y calls x.__le__(y), x==y calls x.__eq__(y),
    x!=y calls x.__ne__(y), x>y calls x.__gt__(y), and x>=y calls x.__ge__(y).
    """

    def __lt__(self, other):
        return False

    def __le__(self, other):
        return False

    def __gt__(self, other):
        return False

    def __ge__(self, other):
        return False

class PersonWithLimitedSkills:
    """
    Make class which is limited to 2 actions - eat and sleep
    Any other attributes addition should result in an error.
    """

    __slots__ = ('eat', 'sleep')


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
    def __init__(self, param):
        self.param = param

    def __call__(self, *args, **kwargs):
        return self.param(*args, **kwargs)