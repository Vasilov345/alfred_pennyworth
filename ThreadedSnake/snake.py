from time import sleep
import curses


def main(screen):
    screen.clear()
    sleep(5)


curses.wrapper(main)
