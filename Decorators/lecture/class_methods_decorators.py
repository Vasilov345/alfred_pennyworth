class Methods:

    def imeth(self, x):
        print([self, x])  # Normal instance method: passed a self

    @staticmethod
    def smeth(x):
        print([x])  # Static: no instance passed

    @classmethod
    def cmeth(cls, x):
        print([cls, x])  # Class: gets class, not instance

    @property
    def name(self):
        return 'Bob ' + self.__class__.__name__


obj = Methods()
obj.imeth(1)
obj.smeth(2)
obj.cmeth(3)
print(obj.name)
