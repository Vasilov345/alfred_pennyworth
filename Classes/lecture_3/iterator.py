import time


class Iterator:
    number: int = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.number += 1
        return self.number


class Iterable:

    number: int = 0

    def __getitem__(self, key):
        self.number += 1
        if self.number == 11:
            raise StopIteration
        return self.number


def check_if_object_is_iterable(obj):
    return '__getitem__' in dir(obj)


if __name__ == "__main__":

    iterator_1 = Iterator()

    # for i in iterator_1:
    #     print(i)
    #     if i == 10:
    #         break
    iterator_2 = iter([1, 2, 3, 4])

    print(type(iterator_2))
    print(next(iterator_2))
    print(next(iterator_2))
    print(next(iterator_2))
    print(next(iterator_2))
    print(next(iterator_2))
    print(next(iterator_2))


    # types_to_check = [int, bool, str, list, tuple, dict, set]
    # for step_type in types_to_check:
    #     print(f" {step_type} Iterable {check_if_object_is_iterable(step_type)}")

    # iterable_1 = Iterable()
    # for i in iterable_1:
    #     print(i)
        # time.sleep(0.5)
