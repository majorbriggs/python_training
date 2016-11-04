import re

message = "File saved at 17:23:57"

pattern = "\d\d:\d\d:\d\d"

m = re.search(pattern, message)
if m: # would be None if no match is found
    print(m.group())