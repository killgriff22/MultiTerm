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
    H = 12 if int(time.strftime("%H")) % 12 == 0 else int(
        time.strftime("%H")) % 12
    Hours = f.renderText(time.strftime(
        f"{H}%p/%M/%S"))
    Date = f.renderText(time.strftime("%d/%m/%Y"))
    display.blit(Hours, (w//2-len(Hours.split("\n")[0])//2, h//2-len(Hours.split("\n"))//2), front_modifier=Fore.BLACK +
                 Back.RED, back_modifier=RESET)
    display.blit(Date, (w//2-len(Date.split("\n")[0])//2, h//2+3),
                 front_modifier=Fore.BLACK+Back.RED, back_modifier=RESET)
    displays.draw_all()
