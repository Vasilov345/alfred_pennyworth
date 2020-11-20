from time import sleep
import curses
from collections import namedtuple

Point = namedtuple('Point', ["y", "x"])
point = Point(10, 15)


class Snake(list):

    def __init__(self):
        super().__init__()
        self.extend([Point(5, 5), Point(5, 6), Point(5, 7)])

    def move(self):
        self.append(Point(self[-1].y, self[-1].x + 1))
        self.pop(0)


def print_snake(screen, snake):
    for point in snake:
        screen.addch(*point, '#')


def main(screen):
    snake = Snake()
    print_snake(screen, snake)
    screen.refresh()
    snake.move()
    snake.move()
    screen.clear()
    print_snake(screen, snake)
    screen.refresh()
    sleep(5)


curses.wrapper(main)
