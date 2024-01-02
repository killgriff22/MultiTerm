w,h=os.get_terminal_size()
display = Screen((w-SafeZone[0]*2,h-SafeZone[1]*2),SafeZone)
#display2 = Screen((w,h//2),(0,h//2))
display.fill(info(" "))
#display2.fill(warn(" "))
display.blit("test",(0,0))
displays.screens.append(display)
import datetime
while True:
    display.blit(str(datetime.datetime.now()),(display.size[0]-len(str(datetime.datetime.now())),display.size[1]//2))
    displays.draw_all()