import time


class Programmer:

    def __enter__(self):
        print("Drink coffee")
        return self

    def work(self, hours):
        for i in range(hours):
            print(f"Programmer is working {i} hours. Left hours {hours - i}. ")
            time.sleep(0.5)
        raise TypeError

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("I am done. Need to wash up my cup")


if __name__ == "__main__":
    # Coffee Programmer with classic __enter__ __exit__  methods
    with Programmer() as denys:
        denys.work(hours=10)
