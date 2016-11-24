String formatting
======================


There are two popular ways to format strings in Python

- string :py:meth:`str.format` method
- ``%`` notation

We will cover here only the first method, as it is now considered to be the standard and recommended way.

The basic syntax is:

``template.format(p1, p2, .... , k1=v1, k2=v2)``

where template is a string containing the placeholders that are filled with data (given as positional or keyword arguments, ``p1``, ``k1`` etc.)

Consider the example:

.. code-block:: python

    name = "Bob"
    age = 23
    hobbies = ['Python', 'Programming', 'Tomb Raider']

    string_template = "My name is {}. I am {} years old. My hobbies are {}"

    output_string = string_template.format(name, age, hobbies)

    print(string_template)

    # My name is Bob. I am 23 years old. My hobbies are ['Python', 'Programming', 'Tomb Raider']

Note that ``format()`` accepts data of different types (strings, numbers, lists, dicts etc...) and automatically converts them to their string representation.

For clarity and control over the order of the arguments used in the template, you can mark the placeholders with numbers and keywords:

.. code-block:: python

    import sys
    introduction = "My name is {0}, I'm {1} years old. {0} is a nice name".format("Bob", 23)
    vers = "Hello {name}. This is Python {version}".format(name="Bob", version=sys.version)
    print(introduction)
    print(vers)
    # My name is Bob, I'm 23 years old. Bob is a nice name
    # This is Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)]

To specify number precision and width of the whole substring use the following syntax

.. code-block:: python

    import math
    "Floating point {0:10.3f}".format(math.pi)

- ``0`` is the index of the argument
- ``3`` digits of precision
- ``10`` is the width of the whole "substring"
- ``f`` as it is a floating point number.