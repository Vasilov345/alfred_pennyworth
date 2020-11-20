from time import sleep
import curses
from collections import namedtuple

Point = namedtuple('Point', ["y", "x"])
point = Point(10, 15)


class Snake(list):

    def __init__(self):
        super().__init__()
        self.extend([Point(5, 5), Point(5, 6), Point(5, 7)])
        self.direction = 'R'

    @property
    def head(self):
        return self[-1]

    def move(self):
        if self.direction == 'R':
            self.append(Point(self.head.y, self.head.x + 1))
            self.pop(0)


def print_snake(screen, snake):
    for point in snake:
        screen.addch(*point, '#')


def main(screen):
    snake = Snake()
    for _ in range(10):
        snake.move()
        print_snake(screen, snake)
        screen.refresh()
        sleep(1)
        screen.clear()
    sleep(5)


curses.wrapper(main)
