import time
from contextlib import contextmanager


class TeaProgrammer:
    @staticmethod
    def work(hours):
        for i in range(hours):
            print(f" TeaProgrammer is working {i} hours. Left hours {hours - i}")
            time.sleep(1)


@contextmanager
def tea_programmer():
    try:
        programmer = TeaProgrammer()
        yield programmer
    except Exception:
        print("Programmer is not happy. Finish for today")
    finally:
        print("Lets wash my cup!")


if __name__ == "__main__":
    # Tea Programmer with contextlib package
    with tea_programmer() as pasha:
        pasha.work(hours=5)
