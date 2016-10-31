import random

with open('input.txt', 'w') as f:
    for i in range(10):
        f.write(str(random.randint(1, 10)) + '\n')

with open('input.txt') as f_in, open('output.txt', 'w') as f_out:
    for l in f_in:
        f_out.write(int(l)*"X" + '\n')
