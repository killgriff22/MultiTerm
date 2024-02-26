import sys
from subprocess import *
from MultiTerm import *
w, h = os.get_terminal_size()
display = Screen((w//2,h),(0,0))
display_2 = Screen((w//2,h),(w//2,0))
display.program_thread("./print")
sleep(1)
display_2.program_thread("./print")
sleep(5)
display.stop_program()
sleep(5)
display_2.stop_program()