w,h=os.get_terminal_size()
display = Screen((w-SafeZone[0]*2,h-SafeZone[1]*2),SafeZone)
#display2 = Screen((w,h//2),(0,h//2))
display.fill(info(" "))
#display2.fill(warn(" "))
display.blit("test",(0,0))
displays.screens.append(display)
import datetime
while True:
    time=datetime.datetime.now().strftime("%H:%M:%S %d/%m/%Y")
    display.blit(time,(display.size[0]//2-len(time),display.size[1]//2))
    displays.draw_all()