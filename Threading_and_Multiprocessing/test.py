import threading
from time import sleep
import curses

c = 'A'


def getch(screen):
    global c
    while True:
        c = screen.getch()


def main(screen):
    global c
    tr = threading.Thread(target=getch, args=[screen], daemon=True)
    tr.start()
    max_y, max_x = screen.getmaxyx()
    for i in range(max_x):
        c = screen.getch()
        screen.clear()
        screen.addch(0, i, c)
        screen.refresh()
        sleep(0.5)


curses.wrapper(main)
