from classes import *
w,h=os.get_terminal_size()
display = Screen((w,h),(0,0))
while True:
    try:
        display.draw()
    except KeyboardInterrupt:
        clear()
        exit()