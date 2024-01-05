import datetime
from classes import *
w, h = os.get_terminal_size()
display = Screen((w-SafeZone[0]*2, h-SafeZone[1]*2), SafeZone)
# display2 = Screen((w,h//2),(0,h//2))
# display2.fill(warn(" "))
displays.screens.append(display)
while True:
    time = datetime.datetime.now().strftime("%H:%M:%S %d/%m/%Y")
    display.fill(error(" "))
    display.blit(time+"\nTest\nTest2Test3\nTest4", (display.size[0]//2-len(time), display.size[1]//2),
                 front_modifier=Fore.BLACK+Back.RED, back_modifier=RESET)
    displays.draw_all()
