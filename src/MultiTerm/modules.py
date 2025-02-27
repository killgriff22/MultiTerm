# empty line for popping
import os
try:
    from asciimatics.screen import Screen
    from asciimatics import event as asciimaticsEvent
    import pygame
except:
    os.system("pip install asciimatics pygame")
    from asciimatics.screen import Screen
    from asciimatics import event as asciimaticsEvent
    import pygame
from atexit import register
from time import sleep
import sys
import subprocess
import hashlib
import time
from subprocess import Popen, PIPE
from threading import Thread, Event
class windowfilllerclass:
    def close(a,**args):
        return
pygame.mixer.init()
window = windowfilllerclass()
__exit__ = exit
os.chdir(os.path.dirname(os.path.abspath(__file__)))
clock = pygame.time.Clock()

def clean_exit():
    global window
    window.close()
    
register(clean_exit)

def Init():
    global window
    window = Screen.open()

def empty(*args, **kwargs):
    return


def hash(string: str) -> str:
    return hashlib.sha256(string.encode()).hexdigest()


def load_config() -> dict:
    return exec(compile(open("config.py").read(), "config", "exec"))


def save_config(config: dict) -> None:
    with open("config.py", "w") as f:
        f.write(str(config))
    return


def print_at(x, y, content):
    command = f"\x1b7\x1b[{y};{x}f{content}\x1b8"
    sys.stdout.write(f"\x1b7\x1b[{y};{x}f{content}\x1b8")
    sys.stdout.flush()


def clear():
    os.system("clear")


class Fore:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'


class Back:
    BLACK = '\033[40m'
    RED = '\033[41m'
    GREEN = '\033[42m'
    YELLOW = '\033[43m'
    BLUE = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN = '\033[46m'
    WHITE = '\033[47m'


RESET = '\033[0m'


def info(message: str) -> None:
    return (f"{Fore.BLACK}{Back.BLUE}{message}{RESET}")


def warn(message: str) -> None:
    return (f"{Fore.BLACK}{Back.YELLOW}{message}{RESET}")


def error(message: str) -> None:
    return f"{Fore.BLACK}{Back.RED}{message}{RESET}"


def success(message: str) -> None:
    return (f"{Fore.BLACK}{Back.GREEN}{message}{RESET}")


def configure_safe_zone(display):
    w_base = 0
    h_base = 0
    while True:
        w, h = display.size
        screen = [[" "]*w for _ in range(h)]
        w -= 1
        h -= 1
        poses = [
            ((0+w_base), (0+h_base)), ((w)-w_base,  (h)-h_base), ((0) +
                                                                  w_base, (h)-h_base), ((w)-w_base,  (0)+h_base),
            ((1+w_base), (0+h_base)), ((w-1)-w_base,  (h)-h_base), ((1) +
                                                                    w_base, (h)-h_base), ((w-1)-w_base,  (0)+h_base),
            ((0+w_base), (1+h_base)), ((w)-w_base,  (h-1)-h_base), ((0) +
                                                                    w_base, (h-1)-h_base), ((w)-w_base,  (1)+h_base),
        ]
        for pos in poses:
            display.content[pos[1]][pos[0]] = "█"
        string = f"Current Size: {w-w_base},{h-h_base}"
        pos_x = w//2-len(string)//2
        pos_y = h//2
        for offset, char in enumerate(string):
            display.content[pos_y][pos_x+offset] = char
        # display.clear()
        display.draw()

valid_hex = "0123456789ABCDEF"
def cleanhex(data):  # used for cleaning the hexadecimal color codes for fore_fromhex()
    return ''.join(filter(valid_hex, data.upper()))

def fore_fromhex(hexcode): 

    if hexcode == "#000000":
        return "\033[38;2;0;0;0;48;2;255;255;255m"
    elif hexcode == "#FFFFFF":
        return Fore.BLACK+Back.WHITE
    hexint = int(cleanhex(hexcode), 16)
    return ("\x1B[48;2;{};{};{}m".format(hexint >> 16,
                                         hexint >> 8 & 0xFF,
                                         hexint & 0xFF))
def fore_fromrgb(rgb):

    if rgb == (0,0,0):
        return "\033[38;2;0;0;0;48;2;255;255;255m"
    elif rgb == (255,255,255):
        return Fore.BLACK+Back.WHITE
    r,g,b = rgb
    return (f"\x1B[48;2;{r};{g};{b}m")
keys = {
    # 48-57 : "0-9"
    # 65-90 : "a-z"
    ord("0"): "0",
    ord("1"): "1",
    ord("2"): "2",
    ord("3"): "3",
    ord("4"): "4",
    ord("5"): "5",
    ord("6"): "6",
    ord("7"): "7",
    ord("8"): "8",
    ord("9"): "9",
    ord("a"): "a",
    ord("b"): "b",
    ord("c"): "c",
    ord("d"): "d",
    ord("e"): "e",
    ord("f"): "f",
    ord("g"): "g",
    ord("h"): "h",
    ord("i"): "i",
    ord("j"): "j",
    ord("k"): "k",
    ord("l"): "l",
    ord("m"): "m",
    ord("n"): "n",
    ord("o"): "o",
    ord("p"): "p",
    ord("q"): "q",
    ord("r"): "r",
    ord("s"): "s",
    ord("t"): "t",
    ord("u"): "u",
    ord("v"): "v",
    ord("w"): "w",
    ord("x"): "x",
    ord("y"): "y",
    ord("z"): "z",
}
