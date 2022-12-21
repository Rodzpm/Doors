import curses

door = """
 ___________
|  __   __  |
| |  | |  | |
| |  | |  | | 
| |__| |__| |
|  __   __()|
| |  | |  | |
| |  | |  | |
| |  | |  | |
| |  | |  | |
| |__| |__| |
|___________|
"""

choose = """
 _____ _                                        _                  
/  __ \ |                                      | |                 
| /  \/ |__   ___   ___  ___  ___    __ _    __| | ___   ___  _ __ 
| |   | '_ \ / _ \ / _ \/ __|/ _ \  / _` |  / _` |/ _ \ / _ \| '__|
| \__/\ | | | (_) | (_) \__ \  __/ | (_| | | (_| | (_) | (_) | |   
 \____/_| |_|\___/ \___/|___/\___|  \__,_|  \__,_|\___/ \___/|_|   
"""

from random import randint
import time

class Game:
    def __init__(self):
        self.doors = list()
        self.nb_doors = 3
        self.life = 3
        self.score = 0
        self.column = 0
        self.show_numbers = True
        self.inc_door = 0
    
    def print_choose_text(self, window, w):
        y = 5
        for elt in choose.split("\n"):
            window.win.addstr(y, w // 2 - 33, elt)
            y += 1
    
    def print_door(self, window, y, x, i):
        for elt in door.split("\n"):
            window.win.addstr(y, x, elt)
            y += 1
        if self.column == i:
            window.win.attron(curses.color_pair(2))
        window.win.addstr(y, x + 6, str(i))
        window.win.attroff(curses.color_pair(2))
    
    def print_room(self, window, y, w):
        self.print_choose_text(window, w)
        x = (w - 20 * self.nb_doors) // 2 + 5
        for i in range(self.nb_doors):
            self.print_door(window, y, x + i * 20, i)
    
    def print_numbers(self, window, w, h):
        for i in range(len(self.doors)):
            window.win.clear()
            window.win.addstr(h//2, w//2, str(self.doors[i]))
            window.win.getch()

        self.show_numbers = False
        
    def print_game(self, window):
        while 1:
            window.win.clear()
            h, w = window.win.getmaxyx()
            if self.show_numbers:
                self.doors.append(randint(0,self.nb_doors - 1))
                self.print_numbers(window, w, h)
            self.print_room(window, h // 2 - 5, w)
            window.win.refresh()
            key = window.win.getch()
            if key == 27:
                break
            if key == curses.KEY_LEFT and self.column > 0:
                self.column -= 1
            elif key == curses.KEY_RIGHT and self.column < self.nb_doors - 1:
                self.column += 1
            elif key == curses.KEY_ENTER or key == 10 or key == 13:
                if (self.column == self.doors[self.inc_door]):
                    self.inc_door += 1
                    self.score += 10
                    if (self.inc_door == len(self.doors)):
                        self.inc_door = 0
                        self.show_numbers = True
                else:
                    f = open("best_score.txt", "r")
                    if int(f.read()) < self.score:
                        f.close()
                        f = open("best_score.txt", "w")
                        f.write(str(self.score))
                        f.close()
                    break

