from classes import *
while True:
    SafeZone = eval(compile(open("config.py").read(),"config","eval"))
    w,h=os.get_terminal_size()
    display = Screen((w-SafeZone[0]*2,h-SafeZone[1]*2),SafeZone)
    #display2 = Screen((w,h//2),(0,h//2))
    display.fill(info(" "))
    #display2.fill(warn(" "))
    display.blit("test",(0,0))
    try:
        display.draw()
#        display2.draw()
    except KeyboardInterrupt:
        clear()
        exit()