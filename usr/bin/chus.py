import curses
import os
import terminal.io as IO

printc = IO.printw


def main(s: curses.window, a: list, c: int, o: list):
    """ basic utility to change the user name, nothing too big """
    b = open('usr/user.txt', 'w')
    b.write(' '.join(a))
    b.close()