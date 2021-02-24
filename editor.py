#!/usr/bin/env python3

import curses
from buffer import Buffer
from display import Window
from controller import Controller

def main(stdscr):
    "The main function, wrapped in curses functions"

    # Create color pair for application title
    curses.init_pair(8, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Initialization
    buf = Buffer()
    window = Window()
    controller = Controller()

    # Draw empty screen
    window.draw(buf, stdscr)

    # Main loop
    while True:
        # Get a character from user as an integer
        inp = stdscr.getch()
        controller.process(inp, buf)
        window.draw(buf, stdscr)

# The main function, with good defaults and exeption handling for curses
if __name__ == '__main__':
    curses.wrapper(main)
