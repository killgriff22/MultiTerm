from classes import *
import random
clear()
w, h = os.get_terminal_size()
SafeZone = (3, 1)
display = Screen((w-SafeZone[0]*2, h-SafeZone[1]*2), SafeZone)
while True:
    display.fill(" ")
    for i in range(1000):
        display.blit(" ", (random.randint(0, w), random.randint(0, h)),
                     front_modifier=Back.WHITE, back_modifier=RESET)
    display.draw()
