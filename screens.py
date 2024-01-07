import datetime
from classes import *
from pyfiglet import Figlet
import threading
import discord
import user
exit_flag = threading.Event()
ready_flag = threading.Event()
client = discord.Client()
clear()
f = Figlet("ansi_regular")
w, h = os.get_terminal_size()
SafeZone = (3, 1)
display = Screen((w-SafeZone[0]*2, (h-SafeZone[1]*2)//2), SafeZone)
display2 = Screen((w-SafeZone[0]*2, (h-SafeZone[1]*2)//2),
                  (SafeZone[0], (h-SafeZone[1]*2)//2+SafeZone[1]))


def Time_thread():
    while not exit_flag.is_set():
        display.fill(error(" "))
        time = datetime.datetime.now()
        H = 12 if int(time.strftime("%H")) % 12 == 0 else int(
            time.strftime("%H")) % 12
        Hours = f.renderText(time.strftime(
            f"{H}/%M/%S"))
        ampm = f.renderText(time.strftime("%p"))
        Date = f.renderText(time.strftime("%d/%m/%Y"))
        display.blit(Hours, (display.size[0]//2-len(Hours.split("\n")[0])//2, display.size[1]//2-len(Hours.split("\n"))//2), front_modifier=Fore.BLACK +
                     Back.RED, back_modifier=RESET)
        display.blit(ampm, (display.size[0]//2+len(Hours.split("\n")[0])//2+1, display.size[1]//2-len(ampm.split("\n"))//2),
                     front_modifier=Fore.BLACK+Back.RED, back_modifier=RESET)
        display.blit(Date, (display.size[0]//2-len(Date.split("\n")[0])//2, display.size[1]//2+3),
                     front_modifier=Fore.BLACK+Back.RED, back_modifier=RESET)
    ready_flag.set()


lines = []
maxlen = display2.size[1]
Thread = threading.Thread(target=Time_thread)


@client.event
async def on_ready():
    Thread.start()
    display2.clear()
    display2.draw()


@client.event
async def on_message(message: discord.message.Message):
    lines.append(
        f"{message.guild.name} : {message.author.display_name} : {message.content if len(f'{message.guild.name} : {message.author.display_name} : {message.content}') < display2.size[0] else message.content[:display2.size[0]]}")
    if len(lines) > maxlen:
        lines.pop(0)
    blit = "\n".join(lines)
    display2.blit(blit, (0, 0))
    display2.clear()
    display2.draw()


@client.event
async def on_error():
    input("Press enter to continue...")
    exit_flag.set()
    while not ready_flag.is_set():
        pass
    Thread.join()
    exit()
client.run(user.token)
