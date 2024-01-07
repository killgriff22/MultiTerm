from modules import *
clear()
process = subprocess.Popen(['python3', 'screens.py'])
oldcontent = hash(open("screens.py", "r").read())
try:
    while True:
        subprocess.check_output(
            ["git", "pull"])
        is_same = hash(open("screens.py", "r").read()) == oldcontent
        if is_same:
            time.sleep(1)
        elif process.poll() is not None:
            print("Restarting...")
            process = subprocess.Popen(['python3', 'screens.py'])
        else:
            process.kill()
            process = subprocess.Popen(['python3', 'screens.py'])
            oldcontent = hash(open("screens.py", "r").read())
except KeyboardInterrupt:
    process.kill()
    print("Exiting...")
    exit()
