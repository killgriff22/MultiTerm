import datetime
from classes import *
from pyfiglet import Figlet
import pyfiglet
clear()
f = Figlet("ansi_regular")
w, h = os.get_terminal_size()
SafeZone = (3, 1)
displays = cluster()
display = Screen((w-SafeZone[0]*2, h-SafeZone[1]*2), SafeZone)
displays.screens.append(display)
while True:
    display.fill(error(" "))
    time = datetime.datetime.now()
    Hours = f.renderText(time.strftime("%H/%M/%S"))
    Date = f.renderText(time.strftime("%d/%m/%Y"))
    display.blit(Hours, (0, 0), front_modifier=Fore.BLACK +
                 Back.RED, back_modifier=RESET)
    display.blit(Date, (0, len(Hours.split("\n"))),
                 front_modifier=Fore.BLACK+Back.RED, back_modifier=RESET)
    displays.draw_all()
