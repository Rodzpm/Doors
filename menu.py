import curses
from logo import *

menu = ['Play', 'Scoreboard', 'Exit']

def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    print_logo(stdscr)
    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(2))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(2))
        else:
            stdscr.addstr(y, x, row)
    stdscr.refresh()