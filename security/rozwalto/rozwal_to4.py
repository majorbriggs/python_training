import re

with open('rozwalto4.txt') as f_in:
    txt = f_in.read()
    password = re.findall("(\/\*(.)\*\/)", txt,)
    print("".join([t[1] for t in password]))