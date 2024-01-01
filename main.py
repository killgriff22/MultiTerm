from classes import *
w,h=os.get_terminal_size()
display = Screen((w,h),(0,0))
display.fill(info(" "))
while True:
    try:
        display.draw()
    except KeyboardInterrupt:
        clear()
        exit()