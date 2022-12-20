import curses
from menu import *
from print_center import *
from best_score import *
from game import *
import os

class Win:
    def __init__(self, stdscr):
        self.win = stdscr
        self.basic_color = curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        self.selected_color = curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)

def main(stdscr):
    #Init Window
    window = Win(stdscr)
    curses.curs_set(0)
    window.win.bkgd(' ', curses.color_pair(1))
    current_row = 0
    print_menu(window.win, current_row)
    #Game Loop
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
                print_best_score(window.win)
            else:
                game = Game()
                game.print_game(window)
        print_menu(window.win, current_row)
    #Reset Terminal
    curses.nocbreak()
    window.win.keypad(0)
    curses.echo()
    curses.endwin()
os.environ.setdefault('ESCDELAY', '25')
curses.wrapper(main)
