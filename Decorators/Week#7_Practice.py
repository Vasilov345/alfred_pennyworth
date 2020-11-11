import time
import logging


# different tasks:
# - Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
# (число повторяется столько раз, чему равно). На вход программе передаётся неотрицательное целое число n — столько
# элементов последовательности должна отобразить программа. На выходе ожидается последовательность чисел, записанных через пробел в одну строку.
# Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.
# Sample Input:
# 7
# Sample Output:
# 1 2 2 3 3 3 4

def number_times(number):
    list_num = [i * str(i) for i in range(1, number + 1)]
    f = ''
    for i in list_num:
        f += i
    return ' '.join(f[:number])


# - Напишите программу, которая считывает с консоли числа (по одному в строке) до тех пор,
# пока сумма введённых чисел не будет равна 0 и сразу после этого выводит сумму квадратов всех считанных чисел.
# Гарантируется, что в какой-то момент сумма введённых чисел окажется равной 0, после этого считывание продолжать не нужно.
# В примере мы считываем числа 1, -3, 5, -6, -10, 13; в этот момент замечаем, что сумма этих чисел равна нулю
# и выводим сумму их квадратов, не обращая внимания на то, что остались ещё не прочитанные значения.
# Sample Input:
# 1
# -3
# 5
# -6
# -10
# 13
# 4
# -8
# Sample Output:
# 340

def input_num():
    number = 0
    sq = []
    while True:
        x = int(input('Enter the number: '))
        number += x
        sq.append(x ** 2)
        if number == 0:
            print(sum(sq))
            break


# - Одно из применений множественного наследование – расширение функциональности класса каким-то заранее определенным способом.
# Например, если нам понадобится логировать какую-то информацию при обращении к методам класса.
# Рассмотрим класс Loggable:
# import time
# class Loggable:
#     def log(self, msg):
#         print(str(time.ctime()) + ": " + str(msg))
# У него есть ровно один метод log, который позволяет выводить в лог (в данном случае в stdout) какое-то сообщение,
# добавляя при этом текущее время.
# Реализуйте класс LoggableList, отнаследовав его от классов list и Loggable таким образом,
# чтобы при добавлении элемента в список посредством метода append в лог отправлялось сообщение, состоящее из только что добавленного элемента.

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    logging.basicConfig(level=logging.DEBUG)

    def __init__(self):
        self.__list = []

    def append(self, __object):
        self.__list.append(__object)
        self.log(__object)


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
