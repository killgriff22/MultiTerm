import datetime
from classes import *
from pyfiglet import Figlet
import pyfiglet
f = Figlet("mono12")
w, h = os.get_terminal_size()
SafeZone = (0, 0)
displays = cluster()
display = Screen((w-SafeZone[0]*2, h-SafeZone[1]*2), SafeZone)
# display2 = Screen((w,h//2),(0,h//2))
# display2.fill(warn(" "))
displays.screens.append(display)
while True:
    time = datetime.datetime.now().strftime("%H/%M")
    display.fill(warn(" "))
    display.blit(time, (0, 0), Fore.BLACK+Back.BLUE, RESET)
    displays.draw_all()
