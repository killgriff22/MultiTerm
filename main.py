from classes import *
displays = cluster()
SafeZone = eval(compile(open("config.py").read(),"config","eval"))
exec(compile(open("screens.py").read(),"screens","exec"))
clear()
while True:
    try:
        displays.draw_all()
#        display2.draw()
    except KeyboardInterrupt:
        clear()
        exit()