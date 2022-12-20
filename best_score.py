from print_center import *
import curses

def print_best_score(stdscr):
    while 1:
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        print_center(stdscr, "Your best score is")
        f = open("best_score.txt", "r").read()
        stdscr.addstr(h//2 + 2, w//2 - len(f)//2, f)
        stdscr.refresh()
        t = stdscr.getch()
        if t == 27:
            break
