dictionary = {"first_name": "Bob",
     "last_name": "der Baumeister",
     "occupation":"builder"}


for key, value in dictionary.items():
    print("Value of {} is {}".format(key, value))


for key in dictionary:
    print("Value of {} is {}".format(key, dictionary[key]))

for element in dictionary.items():
    print("Value of {} is {}".format(element[0], element[1]))



A = [1, 2, 3]
B = ['a', 'b', 'c']


for a, b in zip(A, B):
    print("A: {} B: {}".format(a, b))


keys = [1, 2, 3]
values = ['a', 'b', 'c']

d = dict(zip(keys, values))
print(d)

from string import ascii_lowercase

d = dict(enumerate(ascii_lowercase))

print(d)