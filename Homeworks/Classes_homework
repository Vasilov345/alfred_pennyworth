class CustomInt(int):

    def __init__(self, x):
        self.x = x
        super().__init__()

    def __ge__(self, other):
        return self.x <= other

    def __lt__(self, other):
        return self.x > other

    def __le__(self, other):
        return self.x >= other

    def __gt__(self, other):
        return self.x < other


class PersonWithLimitedSkills:
    __slots__ = ["eat", "sleep"]


class HiddenAttrs:

    def __dir__(self):
        return ()

    @staticmethod
    def __dict__():
        return {}


class CallableInstances:

    def __init__(self, x):
        self.x = x

    def __call__(self, *args):
        return self.x(*args)