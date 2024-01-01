import curses
from time import sleep
shell = curses.initscr()
shell.nodelay(True)
try:
     curses.cbreak()
     while True:
            key = shell.getch()
            if key == 119:
                print("key w pressed")
            sleep(0.03)
except KeyboardInterrupt:
     curses.nocbreak()
