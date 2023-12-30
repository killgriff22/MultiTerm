from classes import *
w,h=os.get_terminal_size()
display = screen((w//2,h),(0,0))
#display.fill("8")
display2 = screen((w//2,h),(w//2,0))
#display2.fill("%")
while True:
    try:
        display.draw()
        display2.draw()
    except KeyboardInterrupt:
        clear()
        exit()