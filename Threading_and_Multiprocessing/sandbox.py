from multiprocessing import Queue
from threading import Thread


def do_work(item):
    print(item ** 2)


def worker():
    while True:
        item = q.get()
        do_work(item)


def source():
    for i in range(3):
        yield i


q = Queue()

for i in range(3):
    t = Thread(target=worker)
    t.start()

for i in source():
    q.put(i)

