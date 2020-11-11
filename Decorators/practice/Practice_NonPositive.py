# - Реализуйте класс PositiveList, отнаследовав его от класса list, для хранения положительных целых чисел.
# Также реализуйте новое исключение NonPositiveError.
# В классе PositiveList переопределите метод append(self, x) таким образом, чтобы при попытке добавить
#  неположительное целое число бросалось исключение NonPositiveError и число не добавлялось,
#  а при попытке добавить положительное целое число, число добавлялось бы как в стандартный list.
# В данной задаче гарантируется, что в качестве аргумента x метода append всегда будет передаваться целое число.
# Примечание:
# Положительными считаются числа, строго большие нуля.

class NonPositiveError(Exception):
    pass


class PositiveList(list):
    """Create the class PositiveList with using staticmethod"""

    list = []

    @staticmethod
    def __str__():
        return str(PositiveList.list)

    @staticmethod
    def append(__object):
        if isinstance(__object, int):
            if __object > 0:
                PositiveList.list.append(__object)
            else:
                raise NonPositiveError('Number must be positive')
        else:
            PositiveList.list.append(__object)


class PositiveList(list):
    """Create the class PositiveList with using instance"""

    def __init__(self):
        self.__list = []

    def __str__(self):
        return str(self.__list)

    def append(self, __object):
        if isinstance(__object, int):
            if __object > 0:
                self.__list.append(__object)
            else:
                raise NonPositiveError('Number must be positive')
        else:
            self.__list.append(__object)


class PositiveList(list):
    """Create the class PositiveList with using classmethod"""

    list = []

    @classmethod
    def __str__(cls):
        return str(PositiveList.list)

    @classmethod
    def append(cls, __object):
        if isinstance(__object, int):
            if __object > 0:
                cls.list.append(__object)
            else:
                raise NonPositiveError('Number must be positive')
        else:
            cls.list.append(__object)
