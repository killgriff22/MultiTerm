from os import listdir, system
print("updating pyproject.toml version number...")
with open("pyproject.toml", "r+") as f:
    lines = f.readlines()
    version = lines[5].split("=")[1].strip().split(".")
    version[0] = version[0][-1:]
    version[2] = version[2][:-1]
    version = [int(i) for i in version]
    version[2] += 1
    if version[2] >= 10:
        version[2] = 0
        version[1] += 1
    if version[1] >= 10:
        version[1] = 0
        version[0] += 1
    lines[5] = f'version = "{version[0]}.{version[1]}.{version[2]}"\n'
    lines = "".join(lines)
    f.seek(0)
    f.write(lines)
print("building...")
with open("src/MultiTerm/classes.py", "r+") as f:
    file = f.readlines()
    file[0] = "from .modules import *"
    file = "".join(file)
    f.seek(0)
    f.write(file)
system("python3 -m build")
system("python3 -m twine upload --repository pypi dist/* -u __token__ -p pypi-AgEIcHlwaS5vcmcCJDNjMDE1MzVhLWIzNjMtNDI1My04Yjg2LTViN2ZlYjczNTA1ZQACKlszLCI0MjUzNzQ1NS01YzM5LTRmODMtOGJmZi1iMmI4ZWEwNzU2OTkiXQAABiBQUbEwXSMLY7DBm3ZMvLMGAfgwMGzsKeeP3bdZRq3SIg")
system("git add .")
system("git commit -m 'build'")
system("git push")
with open("src/MultiTerm/classes.py", "r+") as f:
    file = f.readlines()
    file[0] = "from modules import *"
    file = "".join(file)
    f.seek(0)
    f.write(file)