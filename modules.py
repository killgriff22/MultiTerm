import sys
import os
def load_config() -> dict:
    return eval(open("config.py","r").read())
def save_config(config:dict) -> None:
    with open("config.py","w") as f:
        f.write(str(config))
    return
def print_at(x,y,content):
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
def info(message:str) -> None:
    print(f"{Fore.BLACK}{Back.BLUE}{message}{RESET}")
def warn(message:str) -> None:
    print(f"{Fore.BLACK}{Back.YELLOW}{message}{RESET}")
def error(message:str) -> None:
    return f"{Fore.BLACK}{Back.RED}{message}{RESET}"
def success(message:str) -> None:
    print(f"{Fore.BLACK}{Back.GREEN}{message}{RESET}")