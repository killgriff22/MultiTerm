from classes import *
w,h=os.get_terminal_size()
display = Screen((w,h),(0,0))
#display2 = Screen((w,h//2),(0,h//2))
display.fill(info(" "))
#display2.fill(warn(" "))
display.blit("test",(30,30))
while True:
    try:
        display.draw()
#        display2.draw()
    except KeyboardInterrupt:
        clear()
        exit()