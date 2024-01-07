from classes import *
clear()
w, h = os.get_terminal_size()
SafeZone = (3, 1)
display = Screen((w-SafeZone[0]*2, h-SafeZone[1]*2), SafeZone)
while True:
    display.fill(" ")
    display.draw()
