class CustomInt(int):
    """
    Make class for custom int, which will behave "vice versa" for comparison operations:
    e.g., int < int means less then, but custom int < int should equal custom int > int.
    Take into account <, >, >=, <=
    ** try to achieve this without __init__ rewriting
    """


class PersonWithLimitedSkills:
    """
    Make class which is limited to 2 actions - eat and sleep
    Any other attributes addition should result in an error.
    """


class HiddenAttrs:
    """
    Make class which never tells about its attributes.
    Its attribute list is always empty and attributes dictionary is always empty.
    """


class CallableInstances:
    """
    Make class which takes func parameter on initialization, which is a callable that can be passed.
    Then object of this class may be called - callable passed on init will be called with passed parameters.
    """