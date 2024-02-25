import sys
import os
import subprocess
import hashlib
import time
from subprocess import Popen, PIPE
from threading import Thread,Event
from time import sleep

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



class canvas:
    def __init__(self, size: tuple[int, int]) -> None:
        self.size = size
        self.content = [[" "]*size[0] for _ in range(size[1])]

    def fill(self, char: str) -> None:
        for x in range(0, self.size[0]):
            for y in range(0, self.size[1]):
                self.content[y][x] = char
        return

    def blit(self, text: str, pos: tuple[int, int], front_modifier: str = "", back_modifier: str = "") -> None:
        n = self.size[0]
        lines = text.split("\n")
        for y, line in enumerate(lines):
            # If y position is outside of the canvas height, scroll the canvas
            if y+pos[1] >= self.size[1]:
                self.content.pop(0)
                self.content.append([" "]*self.size[0])
                # Adjust y position to be at the bottom of the canvas
                pos = (pos[0], self.size[1]-1)
            for x, char in enumerate(line):
                if x+pos[0] < self.size[0] and y+pos[1] < self.size[1]:
                    self.content[y+pos[1]][x+pos[0]] = front_modifier+char+back_modifier


class Screen(canvas):
    def __init__(self, size: tuple, pos: tuple) -> None:
        super().__init__(size)
        self.pos = pos
        self.program_y = None
        self.program = None
        self.Program_Thread = None
        self.ExitFlag = Event()

    def draw(self) -> None:
        for i, line in enumerate(self.content):
            if len(line)-1 > self.size[0]:
                self.clear()
                print_at(self.pos[0]+1, self.pos[1]+1,
                         f"line {i} too long!\n{len(line)}\ncropping line for next frame!")
                self.content[i] = self.content[i][:-(len(line)-self.size[0])]
                return
            # print(line)
            compiled = "".join(line)
            print_at(self.pos[0]+1, self.pos[1]+i+1, compiled)

    def clear(self) -> None:
        lines = []
        for i in range(self.size[1]):
            lines.append(" "*self.size[0])
        for i, line in enumerate(lines):
            print_at(self.pos[0]+1, self.pos[1]+i+1, line)
    def capture_program(self, program: str, args: list[str] = []) -> None:
        self.ExitFlag.set()
        self.program = Popen([program]+args, shell=True, stdout=PIPE)
        self.program_y = 0
        for line in self.program.stdout:
            self.blit(line.decode("utf-8").strip(), (0, self.program_y))
            self.draw()
            self.program_y += 1
            if not self.ExitFlag.is_set():
                break
        self.program.terminate()
        self.ExitFlag.clear()
    def program_thread(self,program:str,args:list[str]=[]):
        self.Program_Thread = Thread(target=self.capture_program,args=(program,args))
        self.Program_Thread.start()
    def stop_program(self):
        self.ExitFlag.clear()
        self.Program_Thread.join()
        self.Program_Thread = None
        self.program.terminate()
        self.program = None
        self.program_y = None
        self.clear()
        self.draw()
        return


class cluster:
    def __init__(self):
        self.screens = []

    def draw(self, index: int):
        if not index > len(self.screens):
            self.screens[index].draw()

    def draw_all(self):
        for screen in self.screens:
            screen.draw()

    def remove_screen(self, index: int):
        if not index > len(self.screens):
            self.screens[index].clear()
            self.screens.remove(self.screens[index])

clear()
args = sys.argv
pass
if len(args) >= 2:
    name = args[1]
else:
    name = "screens.py"
try:
    while True:
        process = subprocess.Popen(['python3', name])
        oldcontent = hash(open(name, "r").read())
        subprocess.check_output(
            ["git", "pull"])
        is_same = hash(open(name, "r").read()) == oldcontent
        if is_same:
            time.sleep(1)
        elif process.poll() is not None:
            print("Restarting...")
            input(info("Press enter to continue restarting..."))
            process = subprocess.Popen(['python3', name])
        else:
            process.kill()
            process = subprocess.Popen(['python3', name])
            oldcontent = hash(open(name, "r").read())
except KeyboardInterrupt:
    process.kill()
    print("Exiting...")
    exit()

