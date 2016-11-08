
name = "Bob"
age = 23
hobbies = ['Python', 'Programming', 'Travels']
string_template = "My name is {}. I am {} years old. My hobbies are {}"
output_string = string_template.format(name, age, hobbies)
print(string_template)

import sys

version_string = "This is Python in version {version}".format(version=sys.version)
introduction = "My name is {0}, I'm {1} years old. {0} is a nice name".format("Bob", 23)
print(version_string)
print(introduction)

import math
print("Floating point {0:10.3f}".format(math.pi))