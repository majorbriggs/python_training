.. _args_kwargs:

\*args and \*\*kwargs
==========================

What are function arguments with an asterisk?
----------------------------------------------

On definition of a function, the list arguments may contain elements with one or two asterisks (\*). Traditionally they are named ``args`` and ``kwargs`` respectively.
``*args`` and ``**kwargs`` allow the function to accept variable number of arguments.

Consider the example:

.. code-block:: python

    def print_arguments(*args, **kwargs):
        print("Positional arguments")
        for arg in args:
            print(arg)

        print("Keyword arguments")
        for kwarg, value in kwargs.items():
            print("{} = {}".format(kwarg, value))


    print_arguments(1, 2, x=12, y=14, z=['a', 'b', 'c'])

Gives the output:

.. code-block:: none

    Positional arguments
    1
    2
    Keyword arguments
    y = 14
    x = 12
    z = ['a', 'b', 'c']

So, within the function body:

- optional **positional** arguments, marked with \* are represented as a *list*.
- optional **keyword** arguments, marked with \*\* are represented as a *dictionary*.


The names ``args`` and ``kwargs`` are only customary names, optional arguments can be marked with any valid python object name
(``**keywords``, ``**properties``, ``**optional`` etc..)


Unpacking variables to function arguments
-------------------------------------------------

Similarily, when calling a function, you can pass multiple arguments from a list or a dicrionary as its arguments using **unpacking**

See the example:

.. code-block:: python

    def f(i, j, k):
        print("Got three arguments, {}, {}, {}".format(i, j, k))

    x = (1, 2, 3)

    a, b, c = x  # using unpacking on assignment

    f(*x)  # unpack the list x into positional arguments of f

    # -> Got three arguments, 1, 2, 3

    keyword_arguments = {"i": 10, "j": 20, "k":30}

    f(**keyword_arguments)  # unpack the dict into the fuction arguments

    # -> Got three arguments, 10, 20, 30