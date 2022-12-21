from print_center import *
import curses

def print_best_score(stdscr):
    while 1:
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        print_center(stdscr, "Your best score is")
        f = open("best_score.txt", "r")
        score = f.read()
        stdscr.addstr(h//2 + 2, w//2 - len(score)//2, score)
        f.close()
        stdscr.refresh()
        t = stdscr.getch()
        if t == 27:
            break
