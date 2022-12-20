import curses
from menu import *
from print_center import *
from best_score import *


def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    current_row = 0
    print_menu(stdscr, current_row)

    while 1:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if menu[current_row] == "Exit":
                break
            elif menu[current_row] == "Scoreboard":
                print_best_score(stdscr)
            else:
                print_center(stdscr, "You selected '{}'".format(menu[current_row]))
                stdscr.getch()
        print_menu(stdscr, current_row)
    curses.nocbreak()
    stdscr.keypad(0)
    curses.echo()
    curses.endwin()

curses.wrapper(main)
