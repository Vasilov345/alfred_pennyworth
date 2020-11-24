import curses
from curses import KEY_LEFT, KEY_DOWN, KEY_RIGHT, KEY_UP
import random
from time import sleep
from collections import namedtuple

Point = namedtuple('Point', ["y", "x"])
ARROWS = [KEY_DOWN, KEY_UP, KEY_RIGHT, KEY_LEFT]


# class Food:
#     def __init__(self, sh, sw):
#         self.x = random.randint(0, sw - 2)
#         self.y = random.randint(0, sh - 2)
#
#     def print_food(self, screen):
#         screen.addch(self.y, self.x, '❄')


class Snake(list):

    def __init__(self):
        super().__init__()
        self.extend([Point(5, 5), Point(5, 6), Point(5, 7)])
        self.direction = None

    @property
    def head(self):
        return self[-1]

    def move(self, screen):
        key = screen.getch()

        if key in ARROWS:
            self.direction = key

        if self.direction == KEY_RIGHT:
            self.pop(0)
            self.append(Point(self.head.y, self.head.x + 2))

        if self.direction == KEY_LEFT:
            self.pop(0)
            self.append(Point(self.head.y, self.head.x - 2))

        if self.direction == KEY_DOWN:
            self.pop(0)
            self.append(Point(self.head.y + 1, self.head.x))

        if self.direction == KEY_UP:
            self.pop(0)
            self.append(Point(self.head.y - 1, self.head.x))


def print_snake(screen, snake):
    for point in snake[:-1]:
        screen.addch(*point, '🍊')
    screen.addch(snake[-1][0], snake[-1][1], '🎅')  # '\U0001F600'- emoji


def main(screen):
    sh, sw = screen.getmaxyx()  # sh - screen height, sw - screen weight
    curses.curs_set(0)  # Hides cursor
    screen.nodelay(1)  # Allow don`t wait for user input
    snake = Snake()
    # food = Food(sh, sw)

    while True:
        snake.move(screen)
        # food.print_food(screen)
        print_snake(screen, snake)
        screen.refresh()
        sleep(0.1)
        screen.clear()

        # if snake.head.y == food and snake.head.x == food.x:
        #     screen.addch(snake[0][0], snake[0][1], '#')

        if snake[0] in snake[1:]:
            msg = 'Game over'
            screen.addstr(sh // 2, sw // 2 - len(msg) // 2, msg)
            screen.nodelay(0)
            screen.getch()
            break
            
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
