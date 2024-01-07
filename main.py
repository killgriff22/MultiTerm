from modules import *
clear()
args = sys.argv
pass
if len(args) >= 2:
    if len(args) > 2:
        name = args[1:]
    else:
        name = args[1]
else:
    name = "screens.py"
try:
    if type(name) == list:
        oldcontent = {}
        for n in name:
            process = subprocess.Popen(['python3', n])
            oldcontent[n] = hash(open(n, "r").read())
        while True:
            subprocess.check_output(
                ["git", "pull"])
            for i in name:
                is_same = hash(open(i, "r").read()) == oldcontent[i]
                if is_same:
                    time.sleep(1)
                elif process.poll() is not None:
                    print("Restarting...")
                    process = subprocess.Popen(['python3', i])
                else:
                    process.kill()
                    process = subprocess.Popen(['python3', i])
                    oldcontent[i] = hash(open(i, "r").read())
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
            process = subprocess.Popen(['python3', name])
        else:
            process.kill()
            process = subprocess.Popen(['python3', name])
            oldcontent = hash(open(name, "r").read())
except KeyboardInterrupt:
    process.kill()
    print("Exiting...")
    exit()
