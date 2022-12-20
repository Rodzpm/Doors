logo = """
 __________
|  __  __  |
| |  ||  | |
| |  ||  | | ______ _____  ___________  _____ 
| |__||__| | |  _  \  _  ||  _  | ___ \/  ___|
|  __  __()| | | | | | | || | | | |_/ /\ `--. 
| |  ||  | | | | | | | | || | | |    /  `--. \\
| |  ||  | | | |/ /\ \_/ /\ \_/ / |\ \ /\__/ /
| |  ||  | | |___/  \___/  \___/\_| \_|\____/
| |  ||  | |
| |__||__| |
|__________| 
"""

def print_logo(stdscr):
    y = 5
    l = logo.split("\n")
    h, w = stdscr.getmaxyx()
    for elt in l:
        stdscr.addstr(y, w//2 - 22, elt)
        y += 1 