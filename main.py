from modules import *
clear()
process = subprocess.Popen(['python3', 'screens.py'])
oldcontent = hash(open("screens.py", "r").read())
while True:
    if hash(open("screens.py", "r").read()) == oldcontent:
        pass
    else:
        process.kill()
        process = subprocess.Popen(['python3', 'screens.py'])
        oldcontent = hash(open("screens.py", "r").read())
