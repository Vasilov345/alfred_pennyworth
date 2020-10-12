class CustomInt(int):

    def __init__(self, x):
        self.x = x
        super().__init__()

    def __ge__(self, other):
        if self.x <= other:
            return True
        if self.x >= other:
            return False

    def __lt__(self, other):
        if self.x < other:
            return False
        if self.x > other:
            return True

    def __le__(self, other):
        if self.x <= other:
            return False
        if self.x >= other:
            return True

    def __gt__(self, other):
        if self.x > other:
            return False
        if self.x < other:
            return True


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
