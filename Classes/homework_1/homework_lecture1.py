class CustomInt(int):

    def __init__(self, x):
        self.x = x


    def __lt__(self, other):
        return self.x > self.x

    def __gt__(self, other):
        return self.x < other.x

    def __le__(self, other):
        return self.x >= other.x

    def __ge__(self, other):
        return self.x <= other.x


class PersonWithLimitedSkills:
    __slots__ = ("eat", "sleep")






class HiddenAttrs:
    def __dir__(self):
        return []

    def __dict__(self):
        return {}


class CallableInstances:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)
