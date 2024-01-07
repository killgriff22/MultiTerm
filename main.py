from modules import *
clear()
args = sys.argv
if len(args) >= 2:
    name = args[1]
else:
    name = "screens.py"
process = subprocess.Popen(['python3', name])
oldcontent = hash(open(name, "r").read())
try:
    while True:
        subprocess.check_output(
            ["git", "pull"])
        is_same = hash(open(name, "r").read()) == oldcontent
        if is_same:
            time.sleep(1)
        elif process.poll() is not None:
            print("Restarting...")
            process = subprocess.Popen(['python3', name])
        else:
            process.kill()
            process = subprocess.Popen(['python3', name])
            oldcontent = hash(open(name, "r").read())
except KeyboardInterrupt:
    process.kill()
    print("Exiting...")
    exit()
