password = "adeabecc"
p = []
for (c1, c2) in zip("password", "adeabecc"):
    p.append(chr(ord(c1)+ord(c2)-97))

print("".join(p))


a = 0x12341234
b = 0xadeabecc

print(hex(a ^ b))

for i in range(40):
    print("{}: ROZWAL.txt.tmp_name".format(i))