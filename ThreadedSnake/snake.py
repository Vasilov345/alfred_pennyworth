from time import sleep
import curses
from collections import namedtuple

Point = namedtuple('Point', ["y", "x"])
point = Point(10, 15)


class Snake(list):

    def __init__(self):
        super().__init__()
        self.extend([Point(5, 5), Point(5, 6), Point(5, 7)])


def main(screen):
    for i in Snake():
        screen.addch(*i, '#')
        sleep(1)
    screen.refresh()
    # screen.clear()
    sleep(5)


curses.wrapper(main)
