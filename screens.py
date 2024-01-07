from classes import *
import random
clear()
w, h = os.get_terminal_size()
SafeZone = (3, 1)
display = Screen((w-SafeZone[0]*2, h-SafeZone[1]*2), SafeZone)
while True:
    display.fill(error(" "))
    for i in range(1000):
        display.content[0][1] = Back.WHITE+" "+RESET
    display.draw()
