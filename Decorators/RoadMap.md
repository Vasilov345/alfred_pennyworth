Decorators:

1. there is a bridge function, and Person objects are trying to pass it.
every Person has some money, but the bridge is decorated by Troll (function/class), 
which decrements the sum of money person had before passing the bridge.
If person has no more money, exception TrollIsAngry is raised.

2. decorator as a class
class Timer: 
  
    def __init__(self, func): 
        self.function = func 
  
    def __call__(self, *args, **kwargs): 
        # output execution time for the function
  
  
# adding a decorator to the function 
@Timer
def some_function(delay): 
    from time import sleep 
  
    # Introducing some time delay to  
    # simulate a time taking function. 
    sleep(delay) 
  
some_function(3)

3. recursion + factorial
The following program uses a decorator function to ensure that the argument passed to the function factorial is a positive integer:
def argument_test_natural_number(f):
    # check is arg to f is int and > 0, raise error otherwise
    
@argument_test_natural_number
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

for i in range(1,10):
	print(i, factorial(i))

print(factorial(-1))  # should raise error.


different tasks:
- Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (число повторяется столько раз, чему равно). На вход программе передаётся неотрицательное целое число n — столько элементов последовательности должна отобразить программа. На выходе ожидается последовательность чисел, записанных через пробел в одну строку. 
Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.
Sample Input:
7
Sample Output:
1 2 2 3 3 3 4

- Напишите программу, которая считывает с консоли числа (по одному в строке) до тех пор, 
пока сумма введённых чисел не будет равна 0 и сразу после этого выводит сумму квадратов всех считанных чисел.
Гарантируется, что в какой-то момент сумма введённых чисел окажется равной 0, после этого считывание продолжать не нужно.
В примере мы считываем числа 1, -3, 5, -6, -10, 13; в этот момент замечаем, что сумма этих чисел равна нулю 
и выводим сумму их квадратов, не обращая внимания на то, что остались ещё не прочитанные значения.
Sample Input:
1
-3
5
-6
-10
13
4
-8
Sample Output:
340

- Одно из применений множественного наследование – расширение функциональности класса каким-то заранее определенным способом. 
Например, если нам понадобится логировать какую-то информацию при обращении к методам класса.
Рассмотрим класс Loggable:
import time
class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))
У него есть ровно один метод log, который позволяет выводить в лог (в данном случае в stdout) какое-то сообщение, 
добавляя при этом текущее время.
Реализуйте класс LoggableList, отнаследовав его от классов list и Loggable таким образом, 
чтобы при добавлении элемента в список посредством метода append в лог отправлялось сообщение, состоящее из только что добавленного элемента.

- Реализуйте класс PositiveList, отнаследовав его от класса list, для хранения положительных целых чисел.
Также реализуйте новое исключение NonPositiveError.
В классе PositiveList переопределите метод append(self, x) таким образом, чтобы при попытке добавить
 неположительное целое число бросалось исключение NonPositiveError и число не добавлялось, 
 а при попытке добавить положительное целое число, число добавлялось бы как в стандартный list.
В данной задаче гарантируется, что в качестве аргумента x метода append всегда будет передаваться целое число.
Примечание:
Положительными считаются числа, строго большие нуля.

