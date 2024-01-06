from modules import *
clear()
process = subprocess.Popen(['python3', 'screens.py'])
oldcontent = hash(open("screens.py", "r").read())
while True:
    subprocess.check_output(
        ["git", "pull"])
    if hash(open("screens.py", "r").read()) == oldcontent:
        time.sleep(1)
    else:
        process.kill()
        process = subprocess.Popen(['python3', 'screens.py'])
        oldcontent = hash(open("screens.py", "r").read())
